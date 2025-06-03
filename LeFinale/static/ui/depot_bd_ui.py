# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'depot_bd.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableView, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 801, 561))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.DatabaseTab = QTabWidget(self.verticalLayoutWidget)
        self.DatabaseTab.setObjectName(u"DatabaseTab")
        self.DatabaseTab.setIconSize(QSize(16, 16))
        self.DatabaseTab.setDocumentMode(True)
        self.ArrivalTime = QWidget()
        self.ArrivalTime.setObjectName(u"ArrivalTime")
        self.horizontalWidget = QWidget(self.ArrivalTime)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setGeometry(QRect(0, 0, 801, 441))
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.ActionsArrival = QTabWidget(self.horizontalWidget)
        self.ActionsArrival.setObjectName(u"ActionsArrival")
        self.AddArrivalWidget = QWidget()
        self.AddArrivalWidget.setObjectName(u"AddArrivalWidget")
        self.verticalLayoutWidget_2 = QWidget(self.AddArrivalWidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 9, 371, 391))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.AddAIdBusstop = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.AddAIdBusstop.setObjectName(u"AddAIdBusstop")

        self.verticalLayout_2.addWidget(self.AddAIdBusstop)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.AddAIdRoute = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.AddAIdRoute.setObjectName(u"AddAIdRoute")

        self.verticalLayout_2.addWidget(self.AddAIdRoute)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.AddADate = QTimeEdit(self.verticalLayoutWidget_2)
        self.AddADate.setObjectName(u"AddADate")

        self.verticalLayout_2.addWidget(self.AddADate)

        self.line = QFrame(self.verticalLayoutWidget_2)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.AddAButton = QPushButton(self.verticalLayoutWidget_2)
        self.AddAButton.setObjectName(u"AddAButton")

        self.verticalLayout_2.addWidget(self.AddAButton)

        self.ActionsArrival.addTab(self.AddArrivalWidget, "")
        self.EditArrivalWidget = QWidget()
        self.EditArrivalWidget.setObjectName(u"EditArrivalWidget")
        self.verticalLayoutWidget_3 = QWidget(self.EditArrivalWidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 9, 371, 391))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.EditABusstop = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.EditABusstop.setObjectName(u"EditABusstop")

        self.verticalLayout_3.addWidget(self.EditABusstop)

        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.EditARoute = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.EditARoute.setObjectName(u"EditARoute")

        self.verticalLayout_3.addWidget(self.EditARoute)

        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.EditADate = QTimeEdit(self.verticalLayoutWidget_3)
        self.EditADate.setObjectName(u"EditADate")

        self.verticalLayout_3.addWidget(self.EditADate)

        self.line_2 = QFrame(self.verticalLayoutWidget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.EditAButton = QPushButton(self.verticalLayoutWidget_3)
        self.EditAButton.setObjectName(u"EditAButton")

        self.verticalLayout_3.addWidget(self.EditAButton)

        self.ActionsArrival.addTab(self.EditArrivalWidget, "")
        self.DeleteArrivalWidget = QWidget()
        self.DeleteArrivalWidget.setObjectName(u"DeleteArrivalWidget")
        self.verticalLayoutWidget_4 = QWidget(self.DeleteArrivalWidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(9, 9, 371, 391))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.verticalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.DeleteABusstop = QPlainTextEdit(self.verticalLayoutWidget_4)
        self.DeleteABusstop.setObjectName(u"DeleteABusstop")

        self.verticalLayout_4.addWidget(self.DeleteABusstop)

        self.label_11 = QLabel(self.verticalLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)

        self.DeleteARoute = QPlainTextEdit(self.verticalLayoutWidget_4)
        self.DeleteARoute.setObjectName(u"DeleteARoute")

        self.verticalLayout_4.addWidget(self.DeleteARoute)

        self.line_3 = QFrame(self.verticalLayoutWidget_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.DeleteAButton = QPushButton(self.verticalLayoutWidget_4)
        self.DeleteAButton.setObjectName(u"DeleteAButton")

        self.verticalLayout_4.addWidget(self.DeleteAButton)

        self.ActionsArrival.addTab(self.DeleteArrivalWidget, "")

        self.horizontalLayout.addWidget(self.ActionsArrival)

        self.ArrivalTable = QTableView(self.horizontalWidget)
        self.ArrivalTable.setObjectName(u"ArrivalTable")

        self.horizontalLayout.addWidget(self.ArrivalTable)

        icon = QIcon()
        icon.addFile(u"static/img/clock.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DatabaseTab.addTab(self.ArrivalTime, icon, "")
        self.Busstop = QWidget()
        self.Busstop.setObjectName(u"Busstop")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Busstop.sizePolicy().hasHeightForWidth())
        self.Busstop.setSizePolicy(sizePolicy2)
        self.horizontalWidget_2 = QWidget(self.Busstop)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setGeometry(QRect(0, 0, 801, 441))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.ActionsBusstop = QTabWidget(self.horizontalWidget_2)
        self.ActionsBusstop.setObjectName(u"ActionsBusstop")
        self.AddBusstopWidget = QWidget()
        self.AddBusstopWidget.setObjectName(u"AddBusstopWidget")
        self.verticalLayoutWidget_8 = QWidget(self.AddBusstopWidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(9, 9, 371, 391))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.verticalLayoutWidget_8)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_8.addWidget(self.label_15)

        self.AddBBusstop = QPlainTextEdit(self.verticalLayoutWidget_8)
        self.AddBBusstop.setObjectName(u"AddBBusstop")

        self.verticalLayout_8.addWidget(self.AddBBusstop)

        self.label_14 = QLabel(self.verticalLayoutWidget_8)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.AddBName = QPlainTextEdit(self.verticalLayoutWidget_8)
        self.AddBName.setObjectName(u"AddBName")

        self.verticalLayout_8.addWidget(self.AddBName)

        self.label_13 = QLabel(self.verticalLayoutWidget_8)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_8.addWidget(self.label_13)

        self.AddBBusyness = QPlainTextEdit(self.verticalLayoutWidget_8)
        self.AddBBusyness.setObjectName(u"AddBBusyness")

        self.verticalLayout_8.addWidget(self.AddBBusyness)

        self.AddBIsRoof = QCheckBox(self.verticalLayoutWidget_8)
        self.AddBIsRoof.setObjectName(u"AddBIsRoof")

        self.verticalLayout_8.addWidget(self.AddBIsRoof)

        self.line_4 = QFrame(self.verticalLayoutWidget_8)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_4)

        self.AddBButton = QPushButton(self.verticalLayoutWidget_8)
        self.AddBButton.setObjectName(u"AddBButton")

        self.verticalLayout_8.addWidget(self.AddBButton)

        self.ActionsBusstop.addTab(self.AddBusstopWidget, "")
        self.EditBusstopWidget = QWidget()
        self.EditBusstopWidget.setObjectName(u"EditBusstopWidget")
        self.verticalLayoutWidget_9 = QWidget(self.EditBusstopWidget)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(9, 9, 371, 391))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.verticalLayoutWidget_9)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_9.addWidget(self.label_19)

        self.EditBBusstop = QPlainTextEdit(self.verticalLayoutWidget_9)
        self.EditBBusstop.setObjectName(u"EditBBusstop")

        self.verticalLayout_9.addWidget(self.EditBBusstop)

        self.label_18 = QLabel(self.verticalLayoutWidget_9)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_9.addWidget(self.label_18)

        self.EditBName = QPlainTextEdit(self.verticalLayoutWidget_9)
        self.EditBName.setObjectName(u"EditBName")

        self.verticalLayout_9.addWidget(self.EditBName)

        self.label_17 = QLabel(self.verticalLayoutWidget_9)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_9.addWidget(self.label_17)

        self.EditBBusyness = QPlainTextEdit(self.verticalLayoutWidget_9)
        self.EditBBusyness.setObjectName(u"EditBBusyness")

        self.verticalLayout_9.addWidget(self.EditBBusyness)

        self.EditBIsRoof = QCheckBox(self.verticalLayoutWidget_9)
        self.EditBIsRoof.setObjectName(u"EditBIsRoof")

        self.verticalLayout_9.addWidget(self.EditBIsRoof)

        self.line_5 = QFrame(self.verticalLayoutWidget_9)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.EditBButton = QPushButton(self.verticalLayoutWidget_9)
        self.EditBButton.setObjectName(u"EditBButton")

        self.verticalLayout_9.addWidget(self.EditBButton)

        self.ActionsBusstop.addTab(self.EditBusstopWidget, "")
        self.DeleteBusstopWidget = QWidget()
        self.DeleteBusstopWidget.setObjectName(u"DeleteBusstopWidget")
        self.verticalLayoutWidget_10 = QWidget(self.DeleteBusstopWidget)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(9, 9, 371, 391))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.verticalLayoutWidget_10)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_10.addWidget(self.label_20)

        self.DeleteBBusstop = QPlainTextEdit(self.verticalLayoutWidget_10)
        self.DeleteBBusstop.setObjectName(u"DeleteBBusstop")

        self.verticalLayout_10.addWidget(self.DeleteBBusstop)

        self.line_6 = QFrame(self.verticalLayoutWidget_10)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_6)

        self.DeleteBButton = QPushButton(self.verticalLayoutWidget_10)
        self.DeleteBButton.setObjectName(u"DeleteBButton")

        self.verticalLayout_10.addWidget(self.DeleteBButton)

        self.ActionsBusstop.addTab(self.DeleteBusstopWidget, "")

        self.horizontalLayout_3.addWidget(self.ActionsBusstop)

        self.BusstopsTable = QTableView(self.horizontalWidget_2)
        self.BusstopsTable.setObjectName(u"BusstopsTable")

        self.horizontalLayout_3.addWidget(self.BusstopsTable)

        icon1 = QIcon()
        icon1.addFile(u"static/img/busstop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DatabaseTab.addTab(self.Busstop, icon1, "")
        self.Route = QWidget()
        self.Route.setObjectName(u"Route")
        self.horizontalWidget_3 = QWidget(self.Route)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalWidget_3.setGeometry(QRect(0, 0, 801, 441))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.ActionsRoute = QTabWidget(self.horizontalWidget_3)
        self.ActionsRoute.setObjectName(u"ActionsRoute")
        self.AddRouteWidget = QWidget()
        self.AddRouteWidget.setObjectName(u"AddRouteWidget")
        self.verticalLayoutWidget_11 = QWidget(self.AddRouteWidget)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(10, 10, 371, 381))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.verticalLayoutWidget_11)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_11.addWidget(self.label_25)

        self.AddRRoute = QPlainTextEdit(self.verticalLayoutWidget_11)
        self.AddRRoute.setObjectName(u"AddRRoute")

        self.verticalLayout_11.addWidget(self.AddRRoute)

        self.label_24 = QLabel(self.verticalLayoutWidget_11)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_11.addWidget(self.label_24)

        self.AddRLength = QPlainTextEdit(self.verticalLayoutWidget_11)
        self.AddRLength.setObjectName(u"AddRLength")

        self.verticalLayout_11.addWidget(self.AddRLength)

        self.label_23 = QLabel(self.verticalLayoutWidget_11)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_11.addWidget(self.label_23)

        self.AddRNumOfBusstops = QPlainTextEdit(self.verticalLayoutWidget_11)
        self.AddRNumOfBusstops.setObjectName(u"AddRNumOfBusstops")

        self.verticalLayout_11.addWidget(self.AddRNumOfBusstops)

        self.label_21 = QLabel(self.verticalLayoutWidget_11)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_11.addWidget(self.label_21)

        self.AddRNumOfTrolleybusses = QPlainTextEdit(self.verticalLayoutWidget_11)
        self.AddRNumOfTrolleybusses.setObjectName(u"AddRNumOfTrolleybusses")

        self.verticalLayout_11.addWidget(self.AddRNumOfTrolleybusses)

        self.label = QLabel(self.verticalLayoutWidget_11)
        self.label.setObjectName(u"label")

        self.verticalLayout_11.addWidget(self.label)

        self.AddRStart = QTimeEdit(self.verticalLayoutWidget_11)
        self.AddRStart.setObjectName(u"AddRStart")

        self.verticalLayout_11.addWidget(self.AddRStart)

        self.label_22 = QLabel(self.verticalLayoutWidget_11)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_11.addWidget(self.label_22)

        self.AddRFinish = QTimeEdit(self.verticalLayoutWidget_11)
        self.AddRFinish.setObjectName(u"AddRFinish")

        self.verticalLayout_11.addWidget(self.AddRFinish)

        self.line_7 = QFrame(self.verticalLayoutWidget_11)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_7)

        self.AddRButton = QPushButton(self.verticalLayoutWidget_11)
        self.AddRButton.setObjectName(u"AddRButton")

        self.verticalLayout_11.addWidget(self.AddRButton)

        self.ActionsRoute.addTab(self.AddRouteWidget, "")
        self.EditRouteWidget = QWidget()
        self.EditRouteWidget.setObjectName(u"EditRouteWidget")
        self.verticalLayoutWidget_12 = QWidget(self.EditRouteWidget)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(9, 9, 371, 505))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.verticalLayoutWidget_12)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_12.addWidget(self.label_30)

        self.EditRRoute = QPlainTextEdit(self.verticalLayoutWidget_12)
        self.EditRRoute.setObjectName(u"EditRRoute")

        self.verticalLayout_12.addWidget(self.EditRRoute)

        self.label_29 = QLabel(self.verticalLayoutWidget_12)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_12.addWidget(self.label_29)

        self.EditRLength = QPlainTextEdit(self.verticalLayoutWidget_12)
        self.EditRLength.setObjectName(u"EditRLength")

        self.verticalLayout_12.addWidget(self.EditRLength)

        self.label_28 = QLabel(self.verticalLayoutWidget_12)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_12.addWidget(self.label_28)

        self.EditRNumOfBusstops = QPlainTextEdit(self.verticalLayoutWidget_12)
        self.EditRNumOfBusstops.setObjectName(u"EditRNumOfBusstops")

        self.verticalLayout_12.addWidget(self.EditRNumOfBusstops)

        self.label_27 = QLabel(self.verticalLayoutWidget_12)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_12.addWidget(self.label_27)

        self.EditRNumOfTrolleybusses = QPlainTextEdit(self.verticalLayoutWidget_12)
        self.EditRNumOfTrolleybusses.setObjectName(u"EditRNumOfTrolleybusses")

        self.verticalLayout_12.addWidget(self.EditRNumOfTrolleybusses)

        self.label_3 = QLabel(self.verticalLayoutWidget_12)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3)

        self.EditRStart = QTimeEdit(self.verticalLayoutWidget_12)
        self.EditRStart.setObjectName(u"EditRStart")

        self.verticalLayout_12.addWidget(self.EditRStart)

        self.label_26 = QLabel(self.verticalLayoutWidget_12)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_12.addWidget(self.label_26)

        self.EditRFinish = QTimeEdit(self.verticalLayoutWidget_12)
        self.EditRFinish.setObjectName(u"EditRFinish")

        self.verticalLayout_12.addWidget(self.EditRFinish)

        self.line_8 = QFrame(self.verticalLayoutWidget_12)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_8)

        self.EditRButton = QPushButton(self.verticalLayoutWidget_12)
        self.EditRButton.setObjectName(u"EditRButton")

        self.verticalLayout_12.addWidget(self.EditRButton)

        self.ActionsRoute.addTab(self.EditRouteWidget, "")
        self.DeleteRouteWidget = QWidget()
        self.DeleteRouteWidget.setObjectName(u"DeleteRouteWidget")
        self.verticalLayoutWidget_13 = QWidget(self.DeleteRouteWidget)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(9, 9, 371, 391))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.verticalLayoutWidget_13)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_13.addWidget(self.label_31)

        self.DeleteRRoute = QPlainTextEdit(self.verticalLayoutWidget_13)
        self.DeleteRRoute.setObjectName(u"DeleteRRoute")

        self.verticalLayout_13.addWidget(self.DeleteRRoute)

        self.line_9 = QFrame(self.verticalLayoutWidget_13)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_9)

        self.DeleteRButton = QPushButton(self.verticalLayoutWidget_13)
        self.DeleteRButton.setObjectName(u"DeleteRButton")

        self.verticalLayout_13.addWidget(self.DeleteRButton)

        self.ActionsRoute.addTab(self.DeleteRouteWidget, "")

        self.horizontalLayout_4.addWidget(self.ActionsRoute)

        self.RouteTable = QTableView(self.horizontalWidget_3)
        self.RouteTable.setObjectName(u"RouteTable")

        self.horizontalLayout_4.addWidget(self.RouteTable)

        icon2 = QIcon()
        icon2.addFile(u"static/img/trolleybus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DatabaseTab.addTab(self.Route, icon2, "")

        self.verticalLayout.addWidget(self.DatabaseTab)

        self.Console = QLabel(self.verticalLayoutWidget)
        self.Console.setObjectName(u"Console")
        self.Console.setWordWrap(True)

        self.verticalLayout.addWidget(self.Console)

        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.DatabaseTab.setCurrentIndex(2)
        self.ActionsArrival.setCurrentIndex(0)
        self.ActionsBusstop.setCurrentIndex(0)
        self.ActionsRoute.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0442\u0440\u043e\u043b\u043b\u0435\u0439\u0431\u0443\u0441\u043d\u043e\u0433\u043e \u0434\u0435\u043f\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (int):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (int):", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u044f \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 \u043d\u0430 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443 (HH:MM):", None))
        self.AddAButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None))
        self.ActionsArrival.setTabText(self.ActionsArrival.indexOf(self.AddArrivalWidget), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (int):", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (int):", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u044f \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 \u043d\u0430 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443 (HH:MM):", None))
        self.EditAButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None))
        self.ActionsArrival.setTabText(self.ActionsArrival.indexOf(self.EditArrivalWidget), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (int):", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (int):", None))
        self.DeleteAButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f \u043f\u0440\u0438\u0431\u044b\u0442\u0438\u044f", None))
        self.ActionsArrival.setTabText(self.ActionsArrival.indexOf(self.DeleteArrivalWidget), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.DatabaseTab.setTabText(self.DatabaseTab.indexOf(self.ArrivalTime), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (int):", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (str):", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u043e\u0441\u0442\u044c \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (int):", None))
        self.AddBIsRoof.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u043a\u0440\u044b\u0448\u0438", None))
        self.AddBButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443", None))
        self.ActionsBusstop.setTabText(self.ActionsBusstop.indexOf(self.AddBusstopWidget), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (int):", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (str):", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u043e\u0441\u0442\u044c \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (int):", None))
        self.EditBIsRoof.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u043a\u0440\u044b\u0448\u0438", None))
        self.EditBButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443", None))
        self.ActionsBusstop.setTabText(self.ActionsBusstop.indexOf(self.EditBusstopWidget), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 (int):", None))
        self.DeleteBButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0443", None))
        self.ActionsBusstop.setTabText(self.ActionsBusstop.indexOf(self.DeleteBusstopWidget), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.DatabaseTab.setTabText(self.DatabaseTab.indexOf(self.Busstop), QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (int):", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 (int):", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u043a (int):", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0440\u043e\u043b\u043b\u0435\u0439\u0431\u0443\u0441\u0441\u043e\u0432 (int):", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0441\u0442\u0430\u0440\u0442\u0430 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (HH:MM):", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043a\u043e\u043d\u0446\u0430 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (HH:MM):", None))
        self.AddRButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self.ActionsRoute.setTabText(self.ActionsRoute.indexOf(self.AddRouteWidget), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (int):", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 (int):", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u043a (int):", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u0440\u043e\u043b\u043b\u0435\u0439\u0431\u0443\u0441\u0441\u043e\u0432 (int):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0441\u0442\u0430\u0440\u0442\u0430 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (HH:MM):", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043a\u043e\u043d\u0446\u0430 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (HH:MM):", None))
        self.EditRButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self.ActionsRoute.setTabText(self.ActionsRoute.indexOf(self.EditRouteWidget), QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"(PK) \u041d\u043e\u043c\u0435\u0440 \u043c\u0430\u0440\u0448\u0440\u0443\u0442\u0430 (int):", None))
        self.DeleteRButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self.ActionsRoute.setTabText(self.ActionsRoute.indexOf(self.DeleteRouteWidget), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.DatabaseTab.setTabText(self.DatabaseTab.indexOf(self.Route), QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0448\u0440\u0443\u0442", None))
        self.Console.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0443\u0442 \u0432\u044b\u0432\u043e\u0434\u0438\u0442\u044c\u0441\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f.", None))
    # retranslateUi

