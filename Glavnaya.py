# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Glavnaya9.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1430, 746)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Tovar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tovar.setGeometry(QtCore.QRect(70, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Tovar.setFont(font)
        self.pushButton_Tovar.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Tovar.setObjectName("pushButton_Tovar")
        self.pushButton_Sapp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sapp.setGeometry(QtCore.QRect(420, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_Sapp.setFont(font)
        self.pushButton_Sapp.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Sapp.setObjectName("pushButton_Sapp")
        self.pushButton_Prod = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Prod.setGeometry(QtCore.QRect(750, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_Prod.setFont(font)
        self.pushButton_Prod.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Prod.setObjectName("pushButton_Prod")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(1110, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton4.setObjectName("pushButton4")
        self.pushButtonCategory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCategory.setGeometry(QtCore.QRect(290, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonCategory.setFont(font)
        self.pushButtonCategory.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButtonCategory.setObjectName("pushButtonCategory")
        self.pushButton_Dob_Tovar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dob_Tovar.setGeometry(QtCore.QRect(940, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Dob_Tovar.setFont(font)
        self.pushButton_Dob_Tovar.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Dob_Tovar.setObjectName("pushButton_Dob_Tovar")
        self.pushButton_Izmen_Tovar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Izmen_Tovar.setGeometry(QtCore.QRect(1140, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Izmen_Tovar.setFont(font)
        self.pushButton_Izmen_Tovar.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Izmen_Tovar.setObjectName("pushButton_Izmen_Tovar")
        self.polosa2 = QtWidgets.QLabel(self.centralwidget)
        self.polosa2.setGeometry(QtCore.QRect(-20, 70, 1621, 20))
        self.polosa2.setObjectName("polosa2")
        self.polosa2_2 = QtWidgets.QLabel(self.centralwidget)
        self.polosa2_2.setGeometry(QtCore.QRect(-10, 150, 1621, 20))
        self.polosa2_2.setObjectName("polosa2_2")
        self.label_Tovar = QtWidgets.QLabel(self.centralwidget)
        self.label_Tovar.setGeometry(QtCore.QRect(100, 100, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Tovar.setFont(font)
        self.label_Tovar.setObjectName("label_Tovar")
        self.label_Photo = QtWidgets.QLabel(self.centralwidget)
        self.label_Photo.setGeometry(QtCore.QRect(100, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Photo.setFont(font)
        self.label_Photo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_Photo.setObjectName("label_Photo")
        self.label_Art = QtWidgets.QLabel(self.centralwidget)
        self.label_Art.setGeometry(QtCore.QRect(260, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Art.setFont(font)
        self.label_Art.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_Art.setObjectName("label_Art")
        self.label_Name = QtWidgets.QLabel(self.centralwidget)
        self.label_Name.setGeometry(QtCore.QRect(520, 190, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Name.setFont(font)
        self.label_Name.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_Name.setObjectName("label_Name")
        self.label_Category = QtWidgets.QLabel(self.centralwidget)
        self.label_Category.setGeometry(QtCore.QRect(820, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Category.setFont(font)
        self.label_Category.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_Category.setObjectName("label_Category")
        self.label_Ves = QtWidgets.QLabel(self.centralwidget)
        self.label_Ves.setGeometry(QtCore.QRect(990, 190, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Ves.setFont(font)
        self.label_Ves.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_Ves.setObjectName("label_Ves")
        self.label_Cena = QtWidgets.QLabel(self.centralwidget)
        self.label_Cena.setGeometry(QtCore.QRect(1100, 190, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Cena.setFont(font)
        self.label_Cena.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_Cena.setObjectName("label_Cena")
        self.label_Kol = QtWidgets.QLabel(self.centralwidget)
        self.label_Kol.setGeometry(QtCore.QRect(1190, 190, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Kol.setFont(font)
        self.label_Kol.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_Kol.setObjectName("label_Kol")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 1471, 751))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:/Users/Кристина/Downloads/fonn.png"))
        self.label_9.setObjectName("label_9")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 260, 1274, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_9.raise_()
        self.pushButton_Tovar.raise_()
        self.pushButton_Sapp.raise_()
        self.pushButton_Prod.raise_()
        self.pushButton4.raise_()
        self.pushButtonCategory.raise_()
        self.pushButton_Dob_Tovar.raise_()
        self.pushButton_Izmen_Tovar.raise_()
        self.polosa2.raise_()
        self.polosa2_2.raise_()
        self.label_Tovar.raise_()
        self.label_Photo.raise_()
        self.label_Art.raise_()
        self.label_Name.raise_()
        self.label_Category.raise_()
        self.label_Ves.raise_()
        self.label_Cena.raise_()
        self.label_Kol.raise_()
        self.tableWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Tovar.setText(_translate("MainWindow", "Товары"))
        self.pushButton_Sapp.setText(_translate("MainWindow", "Поставщики"))
        self.pushButton_Prod.setText(_translate("MainWindow", "Продажи"))
        self.pushButton4.setText(_translate("MainWindow", "Отчеты"))
        self.pushButtonCategory.setText(_translate("MainWindow", "Категории"))
        self.pushButton_Dob_Tovar.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_Izmen_Tovar.setText(_translate("MainWindow", "Изменить"))
        self.polosa2.setText(_translate("MainWindow", "___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.polosa2_2.setText(_translate("MainWindow", "___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.label_Tovar.setText(_translate("MainWindow", "Товары"))
        self.label_Photo.setText(_translate("MainWindow", "Фото"))
        self.label_Art.setText(_translate("MainWindow", "Артикул"))
        self.label_Name.setText(_translate("MainWindow", "Наименование"))
        self.label_Category.setText(_translate("MainWindow", "Категория"))
        self.label_Ves.setText(_translate("MainWindow", "Вес"))
        self.label_Cena.setText(_translate("MainWindow", "Цена"))
        self.label_Kol.setText(_translate("MainWindow", "Количество"))
