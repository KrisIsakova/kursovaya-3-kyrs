# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dob_sale9.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 488)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 70, 221, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 100, 221, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(20, 270, 191, 31))
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
        self.pushButton1_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton1_3.setGeometry(QtCore.QRect(30, 220, 171, 31))
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
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 130, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 160, 221, 20))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 160, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 47, 13))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.Fon = QtWidgets.QLabel(Dialog)
        self.Fon.setGeometry(QtCore.QRect(-4, -8, 481, 511))
        self.Fon.setText("")
        self.Fon.setPixmap(QtGui.QPixmap("C:/Users/Кристина/Downloads/gobb.png"))
        self.Fon.setObjectName("Fon")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(230, 130, 221, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 190, 221, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Fon.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.pushButton1.raise_()
        self.pushButton1_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.lineEdit_5.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.dateTimeEdit.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Добавить продажу"))
        self.label_4.setText(_translate("Dialog", "Сумма продажи"))
        self.pushButton1.setText(_translate("Dialog", "Добавить продажу"))
        self.pushButton1_3.setText(_translate("Dialog", "Добавить товар"))
        self.label_5.setText(_translate("Dialog", "Дата и время"))
        self.label_6.setText(_translate("Dialog", "Товары"))
        self.label_2.setText(_translate("Dialog", "Номер продажи"))
        self.label_7.setText(_translate("Dialog", "Количество"))
