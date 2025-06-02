import sys

from PyQt6 import QtSql, QtWidgets
from PyQt6.QtSql import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


from depot_bd_ui import Ui_MainWindow
from delete_dialog_ui import Ui_Dialog as Ui_Delete


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        #uic.loadUi("untitled.ui", self)
        
        self.AddAButton.clicked.connect(self.AddArrival)
        self.EditAButton.clicked.connect(self.EditArrival)
        self.DeleteAButton.clicked.connect(self.DeleteArrival)

        self.AddBButton.clicked.connect(self.AddBusstop)
        self.EditBButton.clicked.connect(self.EditBusstop)
        self.DeleteBButton.clicked.connect(self.DeleteBusstop)

        self.AddRButton.clicked.connect(self.AddRoute)
        self.EditRButton.clicked.connect(self.EditRoute)
        self.DeleteRButton.clicked.connect(self.DeleteRoute)

        self.CreateBD()

        self.AddUpdateToArrivalTable()
        self.AddUpdateToBusstopTable()
        self.AddUpdateToRouteTable()
        

    def CreateBD(self):
        self.depotConnection = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.depotConnection.setDatabaseName('./db/depot.db')
        self.depotConnection.open()

        self.CreateBusstopTable()
        self.CreateRouteTable()
        self.CreateArrivalTable()
        

    def Execute(self, queryStr):
        query = QtSql.QSqlQuery(self.depotConnection)
        self.depotConnection.transaction()
        query.exec(queryStr)
        if query.lastError().isValid():
            #self.Console.setText()
            self.depotConnection.rollback()
            raise Exception(f"Query Error: {query.lastError().text()}")
        else:
            self.depotConnection.commit()


    def ExecuteWithPrepare(self, queryStr, values):
        query = QtSql.QSqlQuery(self.depotConnection)
        query.prepare(queryStr)
    
        for value in values:
            query.addBindValue(value)
        
        self.depotConnection.transaction()
        query.exec()
        if query.lastError().isValid():
            #self.Console.setText(f"Query Error: {query.lastError().text()}")
            self.depotConnection.rollback()
            raise Exception(f"Query Error: {query.lastError().text()}")
        else:
            self.depotConnection.commit()


    def CreateArrivalTable(self):
        self.Execute("""
            CREATE TABLE IF NOT EXISTS ARRIVAL (
            at_Busstop_ID integer NOT NULL,
            at_Route_ID integer NOT NULL,
            at_Time TEXT NOT NULL,
            CONSTRAINT "PK_arrival_time" PRIMARY KEY (at_Route_ID, at_Busstop_ID),
            CONSTRAINT "FK_busStop_ID" FOREIGN KEY (at_Busstop_ID)
                REFERENCES BUSSTOP (bs_ID) MATCH SIMPLE
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            CONSTRAINT "FK_route_ID" FOREIGN KEY (at_Route_ID)
                REFERENCES ROUTE (r_ID) MATCH SIMPLE
                ON UPDATE CASCADE
                ON DELETE RESTRICT
            )""")


    def CreateBusstopTable(self):
        self.Execute("""
            CREATE TABLE IF NOT EXISTS BUSSTOP (
            bs_ID integer NOT NULL,
            bs_Name TEXT NOT NULL,
            bs_Busyness integer NOT NULL DEFAULT 0,
            bs_Roof boolean NOT NULL DEFAULT false,
            CONSTRAINT PK_busStop PRIMARY KEY (bs_ID)
            )""")

    def CreateRouteTable(self):
        self.Execute("""
            CREATE TABLE IF NOT EXISTS ROUTE (
            r_ID integer NOT NULL,
            r_Length integer NOT NULL,
            r_BusstopsCount integer NOT NULL,
            r_CarsCount integer NOT NULL,
            r_StartTime TEXT NOT NULL,
            r_StopTime TEXT NOT NULL,
            CONSTRAINT PK_Routes PRIMARY KEY (r_ID)
            )""")


    def AddUpdateToArrivalTable(self):
        self.modelArrival = QtSql.QSqlTableModel(self)
        self.modelArrival.setTable('ARRIVAL')
        self.modelArrival.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
        self.modelArrival.select()
        self.ArrivalTable.setModel(self.modelArrival)

    def AddUpdateToBusstopTable(self):
        self.modelBusstop = QtSql.QSqlTableModel(self)
        self.modelBusstop.setTable('BUSSTOP')
        self.modelBusstop.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
        self.modelBusstop.select()
        self.BusstopsTable.setModel(self.modelBusstop)

    def AddUpdateToRouteTable(self):
        self.modelRoute = QtSql.QSqlTableModel(self)
        self.modelRoute.setTable('ROUTE')
        self.modelRoute.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnFieldChange)
        self.modelRoute.select()
        self.RouteTable.setModel(self.modelRoute)
        
    def AddArrival(self):
        try:
            busstop_id = int(self.AddAIdBusstop.toPlainText())
            route_id = int(self.AddAIdRoute.toPlainText())
            time = self.AddADate.dateTime().toString("HH:mm")


            # костыль в связи с ограниченностью библиотеки SQLITE
            query = QtSql.QSqlQuery(self.depotConnection)
            query.prepare("SELECT COUNT(*) FROM BUSSTOP WHERE bs_ID = ?")
            query.addBindValue(busstop_id)
            if not query.exec() or not query.next() or query.value(0) == 0:
                self.Console.setText("Ошибка: ОСТАНОВКА с указанным ID НЕ СУЩЕСТВУЕТ")
                return
            # костыль в связи с ограниченностью библиотеки SQLITE
            query.prepare("SELECT COUNT(*) FROM ROUTE WHERE r_ID = ?")
            query.addBindValue(route_id)
            if not query.exec() or not query.next() or query.value(0) == 0:
                self.Console.setText("Ошибка: МАРШРУТ с указанным ID НЕ СУЩЕСТВУЕТ")
                return
                
            self.ExecuteWithPrepare(
                "INSERT INTO ARRIVAL (at_Busstop_ID, at_Route_ID, at_Time) VALUES (?, ?, ?)", 
                [busstop_id, route_id, time]
            )
            
            self.modelArrival.select()
            self.Console.setText("РАСПИСАНИЕ с остановкой " + str(busstop_id) + " и маршрутом " + str(route_id) + " было ДОБАВЛЕНО.")
            
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")


    def EditArrival(self):
        try:
            busstop_id = int(self.EditABusstop.toPlainText())
            route_id = int(self.EditARoute.toPlainText())
            time = self.EditADate.dateTime().toString("HH:mm")

            # костыль в связи с ограниченностью библиотеки SQLITE
            query = QtSql.QSqlQuery(self.depotConnection)
            query.prepare("SELECT COUNT(*) FROM ARRIVAL WHERE at_Busstop_ID = ? AND at_Route_ID = ?")
            query.addBindValue(busstop_id)
            query.addBindValue(route_id)
            if not query.exec() or not query.next() or query.value(0) == 0:
                self.Console.setText("Query Error: РАСПИСАНИЯ с указанным ID НЕ СУЩЕСТВУЕТ")
                return

            
                
            self.ExecuteWithPrepare(
                "UPDATE ARRIVAL SET at_Time = ? WHERE at_Busstop_ID = ? AND at_Route_ID = ?", 
                [time, busstop_id, route_id]
            )
            
            self.modelArrival.select()
            self.Console.setText("РАСПИСАНИЕ с остановкой " + str(busstop_id) + " и маршрутом " + str(route_id) + " было ИЗМЕНЕНО.")
            
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")


    def DeleteArrival(self):
        try:
            
            busstop_id = int(self.DeleteABusstop.toPlainText())
            route_id = int(self.DeleteARoute.toPlainText())



            delete_dialog = DeleteDialog(
                self,
                "DELETE FROM ARRIVAL WHERE at_Busstop_ID = ? AND at_Route_ID = ?",
                [busstop_id, route_id],
                "Вы уверены, что хотите УДАЛИТЬ РАСПИСАНИЕ с остановкой " + str(busstop_id) + " и маршрутом " + str(route_id) + "?",
                "РАСПИСАНИЕ с остановкой " + str(busstop_id) + " и маршрутом " + str(route_id) + " было УДАЛЕНО.",
                self.modelArrival
            )
            delete_dialog.show()
                           
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")


    def AddBusstop(self):
        try:
            busstop_id = int(self.AddBBusstop.toPlainText())
            name = self.AddBName.toPlainText()
            busyness = int(self.AddBBusyness.toPlainText())
            roof = self.AddBIsRoof.isChecked()


            
            self.ExecuteWithPrepare(
                "INSERT INTO BUSSTOP (bs_ID, bs_Name, bs_Busyness, bs_Roof) VALUES (?, ?, ?, ?)",
                [busstop_id, name, busyness, roof]
            )
        
            self.modelBusstop.select()
            self.Console.setText("ОСТАНОВКА с номером " + str(busstop_id) + " была ДОБАВЛЕНА.")
            
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")

    def EditBusstop(self):
        try:

            busstop_id = int(self.EditBBusstop.toPlainText())
            name = self.EditBName.toPlainText()
            busyness = int(self.EditBBusyness.toPlainText())
            roof = self.EditBIsRoof.isChecked()


            query = QtSql.QSqlQuery(self.depotConnection)

            if not query.exec() or not query.next() or query.value(0) == 0:
                self.Console.setText("Query Error: ОСТАНОВКА с указанным ID НЕ СУЩЕСТВУЕТ")
                return
            
            self.ExecuteWithPrepare(
                "UPDATE BUSSTOP SET bs_Name = ?, bs_Busyness = ?, bs_Roof = ? WHERE bs_ID = ?",
                [name, busyness, roof, busstop_id]
            )
        
            self.modelBusstop.select()
            self.Console.setText("ОСТАНОВКА с номером " + str(busstop_id) + " была ИЗМЕНЕНА.")
            
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")

    def DeleteBusstop(self):
        try:
            busstop_id = int(self.DeleteBBusstop.toPlainText())


            # костыль в связи с ограниченностью библиотеки SQLITE
            query = QtSql.QSqlQuery(self.depotConnection)
            query.prepare("SELECT COUNT(*) FROM ARRIVAL WHERE at_Busstop_ID = ?")
            query.addBindValue(busstop_id)

            if not query.exec() or not query.next() or query.value(0) != 0:
                self.Console.setText("Query Error: Удалите все пункты РАСПИСАНИЯ с данной ОСТАНОВКОЙ, чтобы иметь возможность удалить её.")
                return




            delete_dialog = DeleteDialog(
                self,
                "DELETE FROM BUSSTOP WHERE bs_ID = ?",
                [busstop_id],
                "Вы уверены, что хотите УДАЛИТЬ ОСТАНОВКУ с номером " + str(busstop_id) + "?",
                "ОСТАНОВКА с номером " + str(busstop_id) + " была УДАЛЕНА.",
                self.modelBusstop
            )
            delete_dialog.show()

            
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")




    def AddRoute(self):
        try:
            route_id = int(self.AddRRoute.toPlainText())
            length = int(self.AddRLength.toPlainText())
            count_of_busstops = int(self.AddRNumOfBusstops.toPlainText())
            count_of_trolleybusses = int(self.AddRNumOfTrolleybusses.toPlainText())
            start_time = self.AddRStart.dateTime().toString("HH:mm")
            stop_time = self.AddRFinish.dateTime().toString("HH:mm")
            

            self.ExecuteWithPrepare(
                "INSERT INTO ROUTE (r_ID, r_Length, r_BusstopsCount, r_CarsCount, r_StartTime, r_StopTime) VALUES (?, ?, ?, ?, ?, ?)",
                [route_id, length, count_of_busstops, count_of_trolleybusses, start_time, stop_time]
            ) 
        
            self.modelRoute.select()
            self.Console.setText("МАРШРУТ с номером " + str(route_id) + " был ДОБАВЛЕН.")
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")
        

    def EditRoute(self):
        try:


            route_id = int(self.EditRRoute.toPlainText())
            length = int(self.EditRLength.toPlainText())
            count_of_busstops = int(self.EditRNumOfBusstops.toPlainText())
            count_of_trolleybusses = int(self.EditRNumOfTrolleybusses.toPlainText())
            start_time = self.EditRStart.dateTime().toString("HH:mm")
            stop_time = self.EditRFinish.dateTime().toString("HH:mm")


            # костыль в связи с ограниченностью библиотеки SQLITE
            query = QtSql.QSqlQuery(self.depotConnection)
            query.prepare("SELECT COUNT(*) FROM ROUTE WHERE r_ID = ?")
            query.addBindValue(route_id)
            if not query.exec() or not query.next() or query.value(0) == 0:
                self.Console.setText("Query Error: МАРШРУТ с указанным ID НЕ СУЩЕСТВУЕТ")
                return
            
            self.ExecuteWithPrepare(
                "UPDATE ROUTE SET r_Length = ?, r_BusstopsCount = ?, r_CarsCount = ?, r_StartTime = ?, r_StopTime = ? WHERE r_ID = ?",
                [length, count_of_busstops, count_of_trolleybusses, start_time, stop_time, route_id]
            ) 
        
            self.modelRoute.select()
            self.Console.setText("МАРШРУТ с номером " + str(route_id) + " был ИЗМЕНЕН.")
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")

    def DeleteRoute(self):
        try:


            route_id = int(self.DeleteRRoute.toPlainText())
            
            # костыль в связи с ограниченностью библиотеки SQLITE
            query = QtSql.QSqlQuery(self.depotConnection)
            query.prepare("SELECT COUNT(*) FROM ARRIVAL WHERE at_Route_ID = ?")
            query.addBindValue(route_id)
            if not query.exec() or not query.next() or query.value(0) != 0:
                self.Console.setText("Query Error: Удалите все пункты РАСПИСАНИЯ с данным МАРШРУТОМ, чтобы иметь возможность удалить его.")
                return


            delete_dialog = DeleteDialog(
                self,
                "DELETE FROM ROUTE WHERE r_ID = ?",
                [route_id],
                "Вы уверены, что хотите УДАЛИТЬ МАРШРУТ с номером " + str(route_id) + "?",
                "МАРШРУТ с номером " + str(route_id) + " был УДАЛЕН.",
                self.modelRoute
            )
            delete_dialog.show()

            
            
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")


class DeleteDialog(QMainWindow, Ui_Delete):
    def __init__(self, parent=None, command=None, mass=None, text=None, text_ok=None, model=None):
        super().__init__(parent)
        self.parent = parent
        self.command = command
        self.mass = mass
        self.text_ok = text_ok
        self.model = model
        self.setupUi(self)
        self.TextDeialog.setText(text)

    def accept(self):
        try:
            self.parent.ExecuteWithPrepare(
                    self.command, self.mass
                )
            self.model.select()
            self.parent.Console.setText(self.text_ok)
            self.close()
        except Exception as e:
            self.Console.setText(f"Query Error: {e}")
        

    def reject(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
