# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Izmen_sale4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 485)
        self.pushButton1_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton1_2.setGeometry(QtCore.QRect(10, 320, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton1_2.setFont(font)
        self.pushButton1_2.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton1_2.setObjectName("pushButton1_2")
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(10, 270, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton1.setObjectName("pushButton1")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 100, 221, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton1_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton1_3.setGeometry(QtCore.QRect(30, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton1_3.setFont(font)
        self.pushButton1_3.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton1_3.setObjectName("pushButton1_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 70, 221, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.Fon_2 = QtWidgets.QLabel(Dialog)
        self.Fon_2.setGeometry(QtCore.QRect(-14, -8, 481, 511))
        self.Fon_2.setText("")
        self.Fon_2.setPixmap(QtGui.QPixmap("C:/Users/Кристина/Downloads/gobb.png"))
        self.Fon_2.setObjectName("Fon_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 160, 221, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 160, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 190, 221, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 130, 221, 20))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Fon_2.raise_()
        self.pushButton1_2.raise_()
        self.pushButton1.raise_()
        self.label_5.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.pushButton1_3.raise_()
        self.lineEdit.raise_()
        self.label_6.raise_()
        self.lineEdit_5.raise_()
        self.label_7.raise_()
        self.verticalLayoutWidget.raise_()
        self.lineEdit_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton1_2.setText(_translate("Dialog", "Удалить продажу"))
        self.pushButton1.setText(_translate("Dialog", "Сохранить изменения"))
        self.label_5.setText(_translate("Dialog", "Дата и время"))
        self.label_2.setText(_translate("Dialog", "Номер продажи"))
        self.label_4.setText(_translate("Dialog", "Сумма продажи"))
        self.label.setText(_translate("Dialog", "Изменить продажу"))
        self.pushButton1_3.setText(_translate("Dialog", "Добавить товар"))
        self.label_6.setText(_translate("Dialog", "Товары"))
        self.label_7.setText(_translate("Dialog", "Количество"))
