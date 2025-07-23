# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(733, 539)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Uni Sans CAPS Heavy")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 10, 421, 61))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"border-radius:0px;\n"
"font-weight:bold;\n"
"font-size:40pt;")
        self.btn_generatelink = QPushButton(self.centralwidget)
        self.btn_generatelink.setObjectName(u"btn_generatelink")
        self.btn_generatelink.setGeometry(QRect(520, 180, 75, 31))
        self.btn_generatelink.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius:7px;\n"
"font-weight:bold;\n"
"font-size:10pt;")
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(630, 280, 75, 21))
        self.btn_delete.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius:7px;\n"
"font-weight:bold;\n"
"font-size:10pt;")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 310, 691, 221))
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: auto;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(230)
        self.tableView.horizontalHeader().setDefaultSectionSize(230)
        self.tableView.verticalHeader().setVisible(False)
        self.line_for_link = QLineEdit(self.centralwidget)
        self.line_for_link.setObjectName(u"line_for_link")
        self.line_for_link.setGeometry(QRect(180, 180, 311, 31))
        self.line_for_link.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius:7px;\n"
"font-weight:bold;\n"
"font-size:10pt;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Link Shortener", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Link Shortener", None))
        self.btn_generatelink.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

