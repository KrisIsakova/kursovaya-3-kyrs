# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Category.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 378)
        self.pushButton_Dob_Category = QtWidgets.QPushButton(Dialog)
        self.pushButton_Dob_Category.setGeometry(QtCore.QRect(120, 260, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Dob_Category.setFont(font)
        self.pushButton_Dob_Category.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Dob_Category.setObjectName("pushButton_Dob_Category")
        self.pushButton_Izmen_Category = QtWidgets.QPushButton(Dialog)
        self.pushButton_Izmen_Category.setGeometry(QtCore.QRect(120, 300, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Izmen_Category.setFont(font)
        self.pushButton_Izmen_Category.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Izmen_Category.setObjectName("pushButton_Izmen_Category")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setObjectName("lineEdit")
        self.label_Fon = QtWidgets.QLabel(Dialog)
        self.label_Fon.setGeometry(QtCore.QRect(-14, -8, 451, 391))
        self.label_Fon.setText("")
        self.label_Fon.setPixmap(QtGui.QPixmap("C:/Users/Кристина/Downloads/Frame 5.png"))
        self.label_Fon.setObjectName("label_Fon")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 91, 361, 161))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.pushButton_Izmen_Category_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Izmen_Category_2.setGeometry(QtCore.QRect(350, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Izmen_Category_2.setFont(font)
        self.pushButton_Izmen_Category_2.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Izmen_Category_2.setObjectName("pushButton_Izmen_Category_2")
        self.pushButton_Izmen_Category_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Izmen_Category_3.setGeometry(QtCore.QRect(130, 340, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Izmen_Category_3.setFont(font)
        self.pushButton_Izmen_Category_3.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton_Izmen_Category_3.setObjectName("pushButton_Izmen_Category_3")
        self.label_Fon.raise_()
        self.pushButton_Dob_Category.raise_()
        self.pushButton_Izmen_Category.raise_()
        self.lineEdit.raise_()
        self.listWidget.raise_()
        self.pushButton_Izmen_Category_2.raise_()
        self.pushButton_Izmen_Category_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Dob_Category.setText(_translate("Dialog", "Добавить категорию"))
        self.pushButton_Izmen_Category.setText(_translate("Dialog", "Изменить категорию"))
        self.lineEdit.setText(_translate("Dialog", "Найти категорию"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "Серьги"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "Ожерелья"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "Кольца"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_Izmen_Category_2.setText(_translate("Dialog", "х"))
        self.pushButton_Izmen_Category_3.setText(_translate("Dialog", "Сбросить фильтрацию"))
