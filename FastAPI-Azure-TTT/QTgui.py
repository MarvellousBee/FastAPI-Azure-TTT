# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QTgui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QKeyEvent)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QFrame)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        self.show_board = True
        MainWindow.resize(635, 452)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.chatbox = QLabel(self.centralwidget)
        self.chatbox.setObjectName(u"chatbox")
        self.chatbox.setGeometry(QRect(410, 10, 211, 371))
        self.chatbox.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.chatbox.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(410, 390, 211, 21))
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(360, 390, 50, 21))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 40, 320, 320))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)


        self.zone_0 = QPushButton(self.gridLayoutWidget)
        self.zone_0.setObjectName(u"zone_0")
        self.zone_0.setFixedHeight(100)
        self.zone_0.setFixedWidth(100)
        self.gridLayout.addWidget(self.zone_0, 0, 0, 1, 1)
        self.zone_0.setStyleSheet("background-image : url(media/zone_empty.png);")



        self.zone_1 = QPushButton(self.gridLayoutWidget)
        self.zone_1.setObjectName(u"zone_1")
        self.zone_1.setFixedHeight(100)
        self.zone_1.setFixedWidth(100)
        self.gridLayout.addWidget(self.zone_1, 0, 1, 1, 1)
        self.zone_1.setStyleSheet("background-image : url(media/zone_empty.png);")

        self.zone_2 = QPushButton(self.gridLayoutWidget)
        self.zone_2.setObjectName(u"zone_2")
        self.gridLayout.addWidget(self.zone_2, 0, 2, 1, 1)
        self.zone_2.setFixedHeight(100)
        self.zone_2.setFixedWidth(100)
        self.zone_2.setStyleSheet("background-image : url(media/zone_empty.png);")

        self.zone_3 = QPushButton(self.gridLayoutWidget)
        self.zone_3.setObjectName(u"zone_3")
        self.gridLayout.addWidget(self.zone_3, 1, 0, 1, 1)
        self.zone_3.setFixedHeight(100)
        self.zone_3.setFixedWidth(100)
        self.zone_3.setStyleSheet("background-image : url(media/zone_empty.png);")

        self.zone_4 = QPushButton(self.gridLayoutWidget)
        self.zone_4.setObjectName(u"zone_4")
        self.gridLayout.addWidget(self.zone_4, 1, 1, 1, 1)
        self.zone_4.setFixedHeight(100)
        self.zone_4.setFixedWidth(100)
        self.zone_4.setStyleSheet("background-image : url(media/zone_empty.png);")

        self.zone_5 = QPushButton(self.gridLayoutWidget)
        self.zone_5.setObjectName(u"zone_5")
        self.gridLayout.addWidget(self.zone_5, 1, 2, 1, 1)
        self.zone_5.setFixedHeight(100)
        self.zone_5.setFixedWidth(100)
        self.zone_5.setStyleSheet("background-image : url(media/zone_empty.png);")

        self.zone_6 = QPushButton(self.gridLayoutWidget)
        self.zone_6.setObjectName(u"zone_6")
        self.gridLayout.addWidget(self.zone_6, 2, 0, 1, 1)
        self.zone_6.setFixedHeight(100)
        self.zone_6.setFixedWidth(100)
        self.zone_6.setStyleSheet("background-image : url(media/zone_empty.png);")

        self.zone_7 = QPushButton(self.gridLayoutWidget)
        self.zone_7.setObjectName(u"zone_7")
        self.gridLayout.addWidget(self.zone_7, 2, 1, 1, 1)
        self.zone_7.setFixedHeight(100)
        self.zone_7.setFixedWidth(100)
        self.zone_7.setStyleSheet("background-image : url(media/zone_empty.png);")

        self.zone_8 = QPushButton(self.gridLayoutWidget)
        self.zone_8.setObjectName(u"zone_9")
        self.gridLayout.addWidget(self.zone_8, 2, 2, 1, 1)
        self.zone_8.setFixedHeight(100)
        self.zone_8.setFixedWidth(100)
        self.zone_8.setStyleSheet("background-image : url(media/zone_empty.png);")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 635, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Client", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi
