from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QLabel, QFileDialog, QComboBox, QSpinBox, QGraphicsPixmapItem, QGraphicsScene, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime, Qt
from Glavnaya import Ui_MainWindow
from Category import Ui_Dialog
from Dob_category import Ui_Dialog as Ui_Dob_Dialog
from Izmen_category import Ui_Dialog as Ui_Izmen_Dialog
from Dob_tovar import Ui_Dialog as Ui_Dob_Tovar_Dialog
from Izmen_tovar import Ui_Dialog as Ui_Izmen_Tovar_Dialog
from Suppliers import Ui_Form as Ui_Suppliers_Form
from Dob_suppliers import Ui_Dialog as Ui_Dob_Sup_Dialog
from Izmen_suppliers import Ui_Dialog as Ui_Izmen_Sup_Dialog
from Sale import Ui_Form as Ui_Sale_Form
from Dob_sale import Ui_Dialog as Ui_Dob_Sale_Dialog
from Izmen_sale import Ui_Dialog as Ui_Izmen_Sale_Dialog
from Otchet import Ui_Form as Ui_Otchet_Form
from Sfor_otchet import Ui_Dialog as Ui_Sfor_otchet_Dialog
import matplotlib.pyplot as plt
from PyQt5.QtGui import QImage, QPixmap
import io
import os
import sys
import sqlite3
from datetime import datetime, timedelta
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegularExpressionValidator
try:
    db = sqlite3.connect('BD')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Tovar")
    cursor.execute("SELECT * FROM Sale")
    cursor.execute("SELECT * FROM Suppliers")
    db.commit()
    print("Подключение к БД успешно")
except sqlite3.Error as e:
    print("Ошибка подключения к БД:", e)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonCategory.clicked.connect(self.show_category)
        self.ui.pushButton_Dob_Tovar.clicked.connect(self.show_dob_tovar)
        self.ui.pushButton_Izmen_Tovar.clicked.connect(self.show_izmen_tovar)
        self.ui.pushButton_Sapp.clicked.connect(self.show_suppliers)
        self.ui.pushButton_Prod.clicked.connect(self.show_sale)
        self.ui.pushButton4.clicked.connect(self.show_otchet)
        self.selected_category = None

        self.update_table()

    def update_table(self):
        if self.selected_category:
            cursor.execute("SELECT * FROM Tovar WHERE Категория = ?", (self.selected_category,))
        else:
            cursor.execute("SELECT * FROM Tovar")

        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0])-1)
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setColumnWidth(0, 150)
        self.ui.tableWidget.setColumnWidth(1, 180)
        self.ui.tableWidget.setColumnWidth(2, 400)
        self.ui.tableWidget.setColumnWidth(3, 180)
        self.ui.tableWidget.setColumnWidth(4, 100)
        self.ui.tableWidget.setColumnWidth(5, 110)
        self.ui.tableWidget.setColumnWidth(6, 100)

        default_row_height = 120
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(default_row_height)

        self.ui.tableWidget.setFont(QFont("Arial", 12))

        for i in range(len(data)):
            for j in range(len(data[i])-1):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

        for i in range(len(data)):
            image_label = QLabel()
            image_path = data[i][0]
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(140, 140)
            image_label.setPixmap(pixmap)
            self.ui.tableWidget.setCellWidget(i, 0, image_label)

            for j in range(len(data[i]) - 1):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

            for i in range(self.ui.tableWidget.rowCount()):
                for j in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(i, j)
                    if item:
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def set_selected_category(self, category):
        self.selected_category = category
        self.update_table()

    def show_sale(self):
        dialog = Sale()
        self.hide()  
        dialog.exec_()  
        self.show() 

    def show_otchet(self):
        dialog = Otchet()
        self.hide()  
        dialog.exec_()  
        self.show()

    def show_suppliers(self):
        dialog = Suppliers()
        self.hide()
        dialog.exec_()
        self.show()

    def show_category(self):
        dialog = Category()
        dialog.setParent(self)
        dialog.exec_()

    def show_dob_tovar(self):
        dialog = DobTovar(self)
        dialog.exec_()

    def show_izmen_tovar(self):
        selected_tovar_articul = self.ui.tableWidget.currentItem()

        if selected_tovar_articul is None:
            QMessageBox.warning(self, "Предупреждение", "Выберите товар для изменения!")
        else:
            dialog = IzmenTovar(selected_tovar_articul, self)
            dialog.exec_()


class Otchet(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Otchet_Form()
        self.ui.setupUi(self)

        self.ui.pushButtonGlavnaya4.clicked.connect(self.show_mainwindow)
        self.ui.pushButtonSupplier4.clicked.connect(self.show_suppliers)
        self.ui.pushSale4.clicked.connect(self.show_sale)
        self.ui.pushButton1_3.clicked.connect(self.show_sfor_otchet)

    def show_sfor_otchet(self):
        try:
            dialog = Sfor_otchet()
            if dialog.exec_() == QDialog.Accepted:
                selected_time_period = dialog.ui.comboBox.currentText()
                selected_category = dialog.ui.comboBox_2.currentText()
                selected_chart_type = dialog.ui.comboBox_3.currentText()

                if selected_time_period == "за последний месяц":
                    start_date = datetime.now() - timedelta(days=30)
                elif selected_time_period == "за последние 3 месяца":
                    start_date = datetime.now() - timedelta(days=90)
                elif selected_time_period == "за последние 6 месяцев":
                    start_date = datetime.now() - timedelta(days=180)
                else:
                    start_date = datetime.now() - timedelta(days=30)  

                query = """
                            SELECT SUM(Sale.Сумма) AS Общая_выручка, Tovar.Категория
                            FROM Sale
                            JOIN Tovar ON Sale.Артикул LIKE '%' || Tovar.Артикул || '%'
                            WHERE Sale.Дата >= ?
                              AND (Tovar.Категория = ? OR ? = 'Выбрать все')
                            GROUP BY Tovar.Категория
                         """

                if selected_category == "Выбрать все":
                    cursor.execute(query, (start_date.strftime('%Y-%m-%d'), selected_category, selected_category))
                else:
                    cursor.execute(query, (start_date.strftime('%Y-%m-%d'), selected_category, selected_category))
                sales_data = cursor.fetchall()

                print("Выбранный период:", selected_time_period)
                print("Выбранная категория:", selected_category)
                print("Выбранный тип графика:", selected_chart_type)
                print("Данные для графика:", sales_data)

                self.show_chart_in_graphics_view(selected_chart_type, sales_data)

        except Exception as e:
            print("Ошибка при формировании отчета:", e)

    def show_chart_in_graphics_view(self, selected_chart_type, sales_data):
        scene = QGraphicsScene()

        pixmap = self.get_pixmap_from_matplotlib(selected_chart_type, sales_data)

        graphics_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(graphics_item)
        self.ui.graphicsView.setScene(scene)

    def get_pixmap_from_matplotlib(self, chart_type, sales_data):
        categories = [data[1] for data in sales_data]
        revenue = [data[0] for data in sales_data]

        plt.figure(figsize=(8, 6))

        if chart_type == "Гистограмма":
            plt.bar(categories, revenue, color='skyblue')
            plt.xlabel('Категории товаров')
            plt.ylabel('Общая выручка')
            plt.title('Гистограмма общей выручки по категориям')
            plt.xticks(rotation=45)
            plt.tight_layout()

        elif chart_type == "Круговая":
            plt.pie(revenue, labels=categories, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.title('Доля выручки по категориям товаров')

        elif chart_type == "График":
            plt.plot(categories, revenue, marker='o', linestyle='-')
            plt.xlabel('Категории товаров')
            plt.ylabel('Общая выручка')
            plt.title('График общей выручки по категориям')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img = QImage.fromData(buf.getvalue())
        pixmap = QPixmap.fromImage(img)
        plt.close()
        buf.close()

        return pixmap

    def show_histogram(self, sales_data):
        categories = [data[1] for data in sales_data]
        revenue = [data[0] for data in sales_data]

        plt.figure(figsize=(10, 6))
        plt.bar(categories, revenue, color='skyblue')
        plt.xlabel('Категории товаров')
        plt.ylabel('Общая выручка')
        plt.title('Гистограмма общей выручки по категориям')
        plt.xticks(rotation=45)
        plt.tight_layout()

        temp_path = 'temporary_graph.png'
        plt.savefig(temp_path)
        plt.close()  

        return temp_path

    def show_pie_chart(self, sales_data):
        categories = [data[1] for data in sales_data]
        revenue = [data[0] for data in sales_data]

        plt.figure(figsize=(8, 8))
        plt.pie(revenue, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Доля выручки по категориям товаров')

        temp_path = 'temporary_graph.png'
        plt.savefig(temp_path)
        plt.close()  

        return temp_path

    def show_plot(self, sales_data):
        categories = [data[1] for data in sales_data]
        revenue = [data[0] for data in sales_data]

        plt.figure(figsize=(10, 6))
        plt.plot(categories, revenue, marker='o', linestyle='-')
        plt.xlabel('Категории товаров')
        plt.ylabel('Общая выручка')
        plt.title('График общей выручки по категориям')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        temp_path = 'temporary_graph.png'
        plt.savefig(temp_path)
        plt.close()  

        return temp_path

    def show_sale(self):
        self.close()
        dialog = Sale()
        dialog.exec_()

    def show_suppliers(self):
        self.close()
        dialog = Suppliers()
        dialog.exec_()

    def show_mainwindow(self):
        self.close()
        dialog = MainWindow()
        dialog.show()

class Sfor_otchet(QDialog):
    def __init__(self):
        try:
            super().__init__()
            self.ui = Ui_Sfor_otchet_Dialog()
            self.ui.setupUi(self)

            self.ui.pushButton4.clicked.connect(self.button4)
            self.fill_time_period()
            self.fill_categories()
            self.fill_chart_types()


        except Exception as e:
            print("Ошибка в инициализации Sfor_otchet:", e)
    def button4(self):
        self.accept()
    def fill_time_period(self):
        try:
            time_periods = ["за последний месяц", "за последние 3 месяца", "за последние 6 месяцев"]
            self.ui.comboBox.addItems(time_periods)

        except Exception as e:
            print("Ошибка при заполнении периода времени:", e)

    def fill_categories(self):
        try:
            categories = self.get_categories_from_database()
            cate = ["Выбрать все"]

            if categories:
                categories = cate + categories
                self.ui.comboBox_2.addItems(categories)
            else:
                self.ui.comboBox_2.addItems(cate)

        except Exception as e:
            print("Ошибка при заполнении категорий:", e)

    def fill_chart_types(self):
        try:
            chart_types = ["Гистограмма", "Круговая", "График"]
            self.ui.comboBox_3.addItems(chart_types)

        except Exception as e:
            print("Ошибка при заполнении типов диаграммы:", e)

    def get_categories_from_database(self):
        try:
            categories = []
            cursor.execute("SELECT Наименование FROM Category")
            categories = cursor.fetchall()
            categories = [category[0] for category in categories]

        except Exception as e:
            print("Ошибка при получении категорий из БД:", e)

        return categories

class Sale(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sale_Form()
        self.ui.setupUi(self)

        self.ui.pushButtonDobSale.clicked.connect(self.show_dob_sale)
        self.ui.pushButtonIzmenSale.clicked.connect(self.show_izmen_sale)
        self.ui.pushButtonGlavnaya2.clicked.connect(self.show_mainwindow)
        self.ui.pushButtonSupp2.clicked.connect(self.show_suppliers)
        self.ui.pushButton4.clicked.connect(self.show_otchet)
        self.update_table_sale()

    def update_table_sale(self):
        cursor.execute("SELECT * FROM Sale")
        data = cursor.fetchall()

    def update_table_sale(self):
        cursor.execute("SELECT * FROM Sale")
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setColumnWidth(0, 220)
        self.ui.tableWidget.setColumnWidth(1, 250)
        self.ui.tableWidget.setColumnWidth(2, 200)
        self.ui.tableWidget.setColumnWidth(3, 240)
        self.ui.tableWidget.setColumnWidth(4, 340)

        self.ui.tableWidget.setFont(QFont("Arial", 12))

        for i in range(len(data)):
            for j in range(len(data[i])):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

        default_row_height = 90
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(default_row_height)

        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(i, j)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def show_suppliers(self):
        self.close()
        dialog = Suppliers()
        dialog.exec_()

    def show_otchet(self):
        self.close()
        dialog = Otchet()
        dialog.exec_()

    def show_mainwindow(self):
        self.close()
        dialog = MainWindow()
        dialog.show()

    def show_dob_sale(self):
        dialog = Dob_Sale(db, cursor, self)
        dialog.exec_()

    def get_selected_sale_data(self):
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()  
            sale_data = {
                'Номер_продажи': self.ui.tableWidget.item(row, 0).text(),  
                'Сумма': self.ui.tableWidget.item(row, 1).text(),
                'Дата': self.ui.tableWidget.item(row, 2).text(),
                'Товары': self.ui.tableWidget.item(row, 3).text(),
                'Количество': self.ui.tableWidget.item(row, 4).text()
            }
            return sale_data
        return None

    def show_izmen_sale(self):
        sale_data = self.get_selected_sale_data()

        if sale_data:
            dialog = Izmen_Sale(db, cursor, sale_data, self)
            dialog.exec_()
        else:
            QMessageBox.warning(self, "Предупреждение", "Выберите продажу для изменения!")


class Dob_Sale(QDialog):
    def __init__(self, db, cursor, parent_window):
        super().__init__()
        self.ui = Ui_Dob_Sale_Dialog()
        self.ui.setupUi(self)
        self.db = db
        self.cursor = cursor
        self.parent_window = parent_window

        try:
            self.ui.pushButton1_3.clicked.connect(self.add_new_article)
            self.ui.pushButton1.clicked.connect(self.save_data)

            self.article_data = []

            self.ui.lineEdit_2.setReadOnly(True)
            self.ui.lineEdit_5.setReadOnly(True)
            self.ui.lineEdit.setReadOnly(True)
            self.ui.dateTimeEdit.setReadOnly(True)

            next_sale_number = self.get_next_sale_number()
            self.ui.lineEdit.setText(str(next_sale_number))

            self.update_lineEdit_5()

            current_datetime = QDateTime.currentDateTime()
            self.ui.dateTimeEdit.setDateTime(current_datetime)

        except Exception as e:
            print("Ошибка при инициализации:", e)

    def add_new_article(self):
        try:
            new_article_combobox = QComboBox()
            self.ui.verticalLayout.addWidget(new_article_combobox)
            self.fill_article_combobox(new_article_combobox)

            quantity_label = QLabel(f"Количество товара {len(self.article_data) + 1}: ")
            quantity_input = QSpinBox()
            quantity_input.setMinimum(1)

            self.ui.verticalLayout.addWidget(quantity_label)
            self.ui.verticalLayout.addWidget(quantity_input)

            self.article_data.append({'combo': new_article_combobox, 'quantity': quantity_input})
            new_article_combobox.currentIndexChanged.connect(self.calculate_total_amount)

            self.update_lineEdit_5()
        except Exception as e:
            print("Ошибка при добавлении нового товара:", e)

    def fill_article_combobox(self, combobox):
        try:
            self.cursor.execute("SELECT Артикул FROM Tovar")
            articles = self.cursor.fetchall()
            combobox.clear()
            for article in articles:
                combobox.addItem(str(article[0]))
        except Exception as e:
            print("Ошибка при заполнении comboBox:", e)

    def get_next_sale_number(self):
        try:
            self.cursor.execute("SELECT MAX(Номер_продажи) FROM Sale")
            last_sale_number = self.cursor.fetchone()[0]
            if last_sale_number is None:
                return 1
            return last_sale_number + 1
        except Exception as e:
            print("Ошибка при получении номера продажи:", e)
            return 1

    def update_lineEdit_5(self):
        total_quantity = sum(int(item['quantity'].value()) for item in self.article_data)
        self.ui.lineEdit_5.setText(str(total_quantity))

    def calculate_total_amount(self):
        total_amount = sum(self.get_price(int(item['combo'].currentText())) * int(item['quantity'].value()) for item in
                           self.article_data)
        self.ui.lineEdit_2.setText(str(total_amount))

    def get_price(self, article):
        try:
            price = self.cursor.execute("SELECT Цена FROM Tovar WHERE Артикул=?", (article,)).fetchone()
            if price:
                return price[0]
        except Exception as e:
            print("Ошибка при получении цены товара:", e)
        return 0

    def save_data(self):
        sale_number = int(self.ui.lineEdit.text())
        sale_datetime = self.ui.dateTimeEdit.dateTime().toString()

        total_quantity = sum(int(item['quantity'].value()) for item in self.article_data)
        total_amount = sum(self.get_price(int(item['combo'].currentText())) * int(item['quantity'].value()) for item in
                           self.article_data)

        try:
            articles = ', '.join(item['combo'].currentText() for item in self.article_data)

            query = "INSERT INTO Sale (Номер_продажи, Сумма, Дата, Артикул, Количество_проданных_товаров) VALUES (?, ?, ?, ?, ?)"
            values = (sale_number, total_amount, sale_datetime, articles, total_quantity)
            self.cursor.execute(query, values)
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)

        self.db.commit()
        QMessageBox.information(self, "Информация", "Продажа успешно добавлена.")
        self.close()
        self.parent_window.update_table_sale()

class Izmen_Sale(QDialog):
    def __init__(self, db, cursor, sale_data, parent_window):
        super().__init__()
        self.ui = Ui_Izmen_Sale_Dialog()
        self.ui.setupUi(self)
        self.db = db
        self.cursor = cursor
        self.parent_window = parent_window
        self.sale_data = sale_data
        self.article_data = [] 

        try:
            self.ui.pushButton1.clicked.connect(self.save_changes)
            self.fill_sale_data()
            self.disable_modification()
            self.ui.pushButton1_3.clicked.connect(self.add_new_article)
            self.ui.pushButton1_2.clicked.connect(self.delete_sale)
        except Exception as e:
            print("Ошибка при инициализации:", e)

    def fill_sale_data(self):
        self.ui.lineEdit.setText(str(self.sale_data['Номер_продажи']))
        self.ui.lineEdit_3.setText(str(self.sale_data['Дата']))
        self.ui.lineEdit_5.setText(str(self.sale_data['Количество']))
        self.ui.lineEdit_2.setText(str(self.sale_data['Сумма']))

    def disable_modification(self):
        self.ui.lineEdit.setEnabled(False)  
        self.ui.lineEdit_3.setEnabled(False)  
        self.ui.lineEdit_5.setEnabled(False)  
        self.ui.lineEdit_2.setEnabled(False)  

    def add_new_article(self):
        try:
            new_article_combobox = QComboBox()
            self.ui.verticalLayout.addWidget(new_article_combobox)
            self.fill_article_combobox(new_article_combobox)

            quantity_label = QLabel(f"Количество товара {len(self.article_data) + 1}: ")
            quantity_input = QSpinBox()
            quantity_input.setMinimum(1)

            self.ui.verticalLayout.addWidget(quantity_label)
            self.ui.verticalLayout.addWidget(quantity_input)

            self.article_data.append({'combo': new_article_combobox, 'quantity': quantity_input})
            new_article_combobox.currentIndexChanged.connect(self.calculate_total_amount)

            self.update_total_quantity()
            self.calculate_total_amount()
        except Exception as e:
            print("Ошибка при добавлении нового товара:", e)

    def fill_article_combobox(self, combobox):
        try:
            self.cursor.execute("SELECT Артикул FROM Tovar")
            articles = self.cursor.fetchall()
            combobox.clear()
            for article in articles:
                combobox.addItem(str(article[0]))
        except Exception as e:
            print("Ошибка при заполнении comboBox:", e)

    def save_changes(self):
        confirmation = QMessageBox.question(self, "Подтверждение", "Вы уверены, что хотите внести изменения в продажу?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            new_tovar = ', '.join(item['combo'].currentText() for item in self.article_data)

            try:
                query = "UPDATE Sale SET Артикул = ? WHERE Номер_продажи = ?"
                values = (new_tovar, self.sale_data['Номер_продажи'])  
                print(values)
                self.cursor.execute(query, values)
                self.db.commit()

                QMessageBox.information(self, "Успех", "Изменения сохранены")
                self.parent_window.update_table_sale()  
                self.close()
            except Exception as e:
                print("Ошибка при сохранении изменений:", e)

    def update_total_quantity(self):
        total_quantity = sum(int(item['quantity'].value()) for item in self.article_data)
        self.ui.lineEdit_5.setText(str(total_quantity))

    def calculate_total_amount(self):
        total_amount = sum(self.get_price(int(item['combo'].currentText())) * int(item['quantity'].value()) for item in self.article_data)
        self.ui.lineEdit_2.setText(str(total_amount))

    def get_price(self, article):
        try:
            price = self.cursor.execute("SELECT Цена FROM Tovar WHERE Артикул=?", (article,)).fetchone()
            if price:
                return price[0]
        except Exception as e:
            print("Ошибка при получении цены товара:", e)
        return 0

    def delete_sale(self):
        confirmation = QMessageBox.question(self, "Удаление", "Вы уверены, что хотите удалить эту продажу?",
                                            QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            try:
                query = "DELETE FROM Sale WHERE Номер_продажи = ?"
                values = (self.sale_data['Номер_продажи'],)
                self.cursor.execute(query, values)
                self.db.commit()

                QMessageBox.information(self, "Успех", "Продажа удалена")
                self.parent_window.update_table_sale()
                self.close()
            except Exception as e:
                print("Ошибка при удалении продажи:", e)


class Suppliers(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Suppliers_Form()
        self.ui.setupUi(self)

        self.ui.pushButtonDob_Sup.clicked.connect(self.show_dob_sup)
        self.ui.pushButtonIzmen_Sapp.clicked.connect(self.show_izmen_sapp)
        self.ui.pushButtonOtchet.clicked.connect(self.show_otchet)
        self.ui.pushButtonSale1.clicked.connect(self.show_sale)
        self.ui.pushButtonGlavnaya.clicked.connect(self.show_mainwindow)
        self.update_table_suppliers()

    def update_table_suppliers(self):
        cursor.execute("SELECT * FROM Suppliers")
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setColumnWidth(0, 300)
        self.ui.tableWidget.setColumnWidth(1, 360)
        self.ui.tableWidget.setColumnWidth(2, 300)
        self.ui.tableWidget.setColumnWidth(3, 290)

        self.ui.tableWidget.setFont(QFont("Arial", 12))

        for i in range(len(data)):
            for j in range(len(data[i])):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

        default_row_height = 90
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(default_row_height)



        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(i, j)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def get_selected_organization_name(self):
        selected_row = self.ui.tableWidget.currentRow()
        org_name_column_index = 1 
        org_name = self.ui.tableWidget.item(selected_row, org_name_column_index).text()
        return org_name

    def show_izmen_sapp(self):
        if self.ui.tableWidget.currentRow() == -1:
            QMessageBox.warning(self, "Предупреждение", "Выберите поставщика для изменения!")
            return

        try:
            org_name = self.get_selected_organization_name()
            dialog = IzmenSup(db_connection=db, org_name=org_name)
            dialog.exec_()
            if dialog.result() == QDialog.Accepted:
                self.update_table_suppliers()
        except Exception as e:
            print("Ошибка при открытии окна IzmenSup:", e)

    def show_dob_sup(self):
        try:
            dialog = DobSup(db_connection=db)
            dialog.suppliers_window = self
            result = dialog.exec_()
            if result == QDialog.Accepted:
                self.update_table_suppliers()
        except Exception as e:
            print("Ошибка при открытии окна DobSup:", e)

    def show_sale(self):
            self.close()
            dialog = Sale()
            dialog.exec_()

    def show_otchet(self):
        self.close()
        dialog = Otchet()
        dialog.exec_()

    def show_mainwindow(self):
            self.close()
            dialog = MainWindow()
            dialog.show()


class DobSup(QDialog):
    def __init__(self, db_connection):
        super().__init__()
        self.ui = Ui_Dob_Sup_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton1_3.clicked.connect(self.add_new_combo_box)
        self.ui.pushButton1.clicked.connect(self.save_changes_sup)

        self.ui.lineEdit_3.setValidator(QIntValidator())
        self.ui.lineEdit_2.setValidator(QRegularExpressionValidator(QtCore.QRegularExpression("[а-яА-Я]*")))
        self.ui.lineEdit.setValidator(QRegularExpressionValidator(QtCore.QRegularExpression("[а-яА-Я]*")))

        self.combo_boxes = []

    def add_new_combo_box(self):
        new_combo_box = QComboBox()
        cursor.execute("SELECT Артикул FROM Tovar")
        articles = cursor.fetchall()
        for article in articles:
            new_combo_box.addItem(str(article[0]))

        self.combo_boxes.append(new_combo_box)
        self.ui.verticalLayout.addWidget(new_combo_box)

    def save_changes_sup(self):
        value_1 = self.ui.lineEdit.text()
        value_2 = self.ui.lineEdit_2.text()
        value_3_text = self.ui.lineEdit_3.text()

        if not (value_1 and value_2 and value_3_text):
            QMessageBox.warning(self, "Предупреждение", "Заполните все поля!")
            return

        try:
            value_3 = int(value_3_text)
        except ValueError:
            QMessageBox.warning(self, "Предупреждение", "Неверный формат данных в поле 'Контактная информация'.")
            return

        selected_articles = []
        for combo_box in self.combo_boxes:
            selected_articles.append(combo_box.currentText())

        articles_string = ', '.join(selected_articles)

        cursor.execute(
            "INSERT INTO Suppliers (ФИО, Наименование_организации, Контактная_информация, Товары) VALUES (?, ?, ?, ?)",
            (value_1, value_2, value_3, articles_string))
        db.commit()
        QMessageBox.information(self, "Информация", "Поставщик добавлен успешно.")
        self.accept()


class IzmenSup(QDialog):
    def __init__(self, db_connection, org_name):
        super().__init__()
        self.ui = Ui_Izmen_Sup_Dialog()
        self.ui.setupUi(self)
        self.org_name = org_name

        self.ui.pushButton1_3.clicked.connect(self.add_new_combo_box)
        self.ui.pushButton1.clicked.connect(self.save_changes_sup)
        self.ui.pushButton1_2.clicked.connect(self.delete_supplier)

        self.ui.lineEdit_3.setValidator(QIntValidator())
        self.ui.lineEdit_2.setValidator(QRegularExpressionValidator(QtCore.QRegularExpression("[а-яА-Я]*")))
        self.ui.lineEdit.setValidator(QRegularExpressionValidator(QtCore.QRegularExpression("[а-яА-Я]*")))

        self.combo_boxes = []

        self.load_organization_data()

    def load_organization_data(self):
        cursor.execute("SELECT * FROM Suppliers WHERE Наименование_организации = ?", (self.org_name,))
        organization_data = cursor.fetchone()

        if organization_data:
            print()
            self.ui.lineEdit.setText(organization_data[0])
            self.ui.lineEdit_2.setText(organization_data[1])
            self.ui.lineEdit_3.setText(str(organization_data[3]))


    def add_new_combo_box(self):
        new_combo_box = QComboBox()
        cursor.execute("SELECT Артикул FROM Tovar")
        articles = cursor.fetchall()
        for article in articles:
            new_combo_box.addItem(str(article[0]))

        self.combo_boxes.append(new_combo_box)
        self.ui.verticalLayout.addWidget(new_combo_box)

    def delete_supplier(self):
        try:
            reply = QMessageBox.question(self, 'Удаление поставщика', 'Вы уверены, что хотите удалить поставщика?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                cursor.execute("DELETE FROM Suppliers WHERE Наименование_организации = ?", (self.org_name,))
                db.commit()
                QMessageBox.information(self, "Информация", "Поставщик успешно удален.")
                self.accept()

        except sqlite3.Error as e:
            print("Ошибка при удалении поставщика из БД:", e)

    def save_changes_sup(self):
        value_1 = self.ui.lineEdit.text()
        value_2 = self.ui.lineEdit_2.text()
        value_3_text = self.ui.lineEdit_3.text()

        if not (value_1 and value_2 and value_3_text):
            QMessageBox.warning(self, "Предупреждение", "Заполните все поля!")
            return

        try:
            value_3 = int(value_3_text)
        except ValueError:
            QMessageBox.warning(self, "Предупреждение", "Неверный формат данных в поле 'Контактная информация'.")
            return

        selected_articles = []
        for combo_box in self.combo_boxes:
            selected_articles.append(combo_box.currentText())

        articles_string = ', '.join(selected_articles)

        cursor.execute(
            "UPDATE Suppliers SET ФИО = ?, Наименование_организации = ?, Контактная_информация = ?, Товары = ? WHERE Наименование_организации = ?",
            (value_1, value_2, value_3, articles_string, self.org_name))

        db.commit()
        QMessageBox.information(self, "Информация", "Изменения сохранены успешно.")
        self.accept()


class DobCategory(QDialog):
    def __init__(self, load_categories_func):
        super().__init__()
        self.ui = Ui_Dob_Dialog()
        self.ui.setupUi(self)
        self.load_categories = load_categories_func
        self.ui.pushButton1_2.clicked.connect(self.save_changes_category)
        self.ui.pushButton1.clicked.connect(self.clear_line_edit)

    def save_changes_category(self):
        value1 = self.ui.lineEdit.text()

        if not value1.strip():
            QMessageBox.critical(self, "Ошибка", "Нельзя добавить пустую категорию. Введите текст")
            return

        if not value1.isalpha():
            QMessageBox.critical(self, "Ошибка", "Введите текст, а не числа или специальные символы")
            return

        try:
            cursor.execute(
                "INSERT INTO Category (Наименование) VALUES (?)",
                (value1,))
            db.commit()
            QMessageBox.information(self, "Информация", "Категория успешно добавлена.")
            self.load_categories()
            self.accept()
            print("Данные успешно добавлены в БД")
        except sqlite3.Error as e:
            print("Ошибка при вставке данных в БД:", e)

    def clear_line_edit(self):
        self.ui.lineEdit.clear()

class IzmenCategory(QDialog):
    def __init__(self, selected_category, load_categories_func, parent=None):
        super().__init__(parent)
        self.ui = Ui_Izmen_Dialog()
        self.ui.setupUi(self)
        self.selected_category = selected_category
        self.load_categories = load_categories_func
        self.ui.lineEdit.setText(selected_category)
        self.ui.pushButton1_2.clicked.connect(self.save_changes)
        self.ui.pushButton1_3.clicked.connect(self.delete_category)

    def save_changes(self):
        new_category_name = self.ui.lineEdit.text()

        if not new_category_name.strip():
            QMessageBox.critical(self, "Ошибка", "Нельзя сохранить пустую категорию")
            return

        if not new_category_name.isalpha():
            QMessageBox.critical(self, "Ошибка", "Введите текст, а не числа или специальные символы")
            return

        try:
            cursor.execute("UPDATE Category SET Наименование = ? WHERE Наименование = ?",
                           (new_category_name, self.selected_category))
            db.commit()
            QMessageBox.information(self, "Информация", "Категория успешно изменена.")
            print("Category updated successfully in the database")
            self.load_categories()
            self.accept()
        except sqlite3.Error as e:
            print("Ошибка при обновлении данных в БД:", e)
    def delete_category(self):
        try:
            reply = QMessageBox.question(self, 'Удаление категории', 'Вы уверены, что хотите удалить категорию?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                selected_category = self.selected_category
                print("Trying to delete category:", selected_category)
                cursor.execute("DELETE FROM Category WHERE UPPER(Наименование) = UPPER(?)", (selected_category,))
                db.commit()
                QMessageBox.information(self, "Информация", "Категория успешно удалена.")
                print("Category deleted successfully from the database")
                self.load_categories()
                self.accept()
        except sqlite3.Error as e:
            print("Ошибка при удалении данных из БД:", e)

class Category(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_Dob_Category.clicked.connect(self.show_dob_category)
        self.ui.pushButton_Izmen_Category.clicked.connect(self.show_izmen_category)
        self.load_categories()
        self.ui.listWidget.itemClicked.connect(self.sort_products_by_category)
        self.ui.lineEdit.textChanged.connect(self.find_category)
        self.ui.pushButton_Izmen_Category_2.clicked.connect(self.close)
        self.ui.pushButton_Izmen_Category_3.clicked.connect(self.reset_filter)

    def find_category(self, text):
        input_text = text.lower()
        for index in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(index)
            if item.text().lower().startswith(input_text):
                self.ui.listWidget.setCurrentItem(item)
                break

    def load_categories(self):
        try:
            cursor.execute("SELECT Наименование FROM Category")
            categories = cursor.fetchall()
            self.ui.listWidget.clear()
            for category in categories:
                self.ui.listWidget.addItem(category[0])
        except sqlite3.Error as e:
            print("Ошибка при извлечении данных из БД:", e)

    def sort_products_by_category(self):
        selected_category = self.ui.listWidget.currentItem().text()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM Tovar
                WHERE Категория = ?
            """, (selected_category,))
            count = cursor.fetchone()[0]

            if count == 0:
                QMessageBox.information(self, "Отсутствие товаров", "Товаров по данной категории нет")
            else:
                main_window = self.parent()
                if main_window:
                    main_window.set_selected_category(selected_category)
                self.accept()

        except sqlite3.Error as e:
            print("Ошибка при проверке наличия товаров в категории:", e)
            QMessageBox.critical(self, "Ошибка", "Ошибка при проверке наличия товаров в категории:\n{}".format(str(e)))
        except Exception as ex:
            print("Непредвиденная ошибка:", ex)
            QMessageBox.critical(self, "Ошибка", "Непредвиденная ошибка:\n{}".format(str(ex)))

    def reset_filter(self):
        self.ui.lineEdit.clear()
        self.ui.listWidget.setCurrentRow(-1)
        self.parent().set_selected_category(None)

    def show_dob_category(self):
        dialog = DobCategory(self.load_categories)
        dialog.exec_()

    def show_izmen_category(self):
        selected_category = self.ui.listWidget.currentItem()
        if selected_category is None:
            QMessageBox.information(self, "Ошибка", "Категория не выбрана для изменения")
        else:
            dialog = IzmenCategory(selected_category.text(), self.load_categories, self)
            dialog.exec_()

class DobTovar(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Dob_Tovar_Dialog()
        self.ui.setupUi(self)
        self.comboboxes()
        self.ui.lineEdit.setValidator(QIntValidator())
        self.ui.lineEdit_2.setValidator(QRegularExpressionValidator(QtCore.QRegularExpression("[а-яА-Я]*")))
        self.ui.lineEdit_4.setValidator(QDoubleValidator())
        self.ui.lineEdit_5.setValidator(QIntValidator())
        self.ui.lineEdit_6.setValidator(QIntValidator())
        self.ui.lineEdit_3.mousePressEvent = self.browse_image
        self.ui.pushButton1.clicked.connect(self.save_changes)

    def comboboxes(self):
        try:
            cursor.execute("SELECT Наименование FROM Category")
            categories = cursor.fetchall()
            self.ui.comboBox.clear()
            for category in categories:
                self.ui.comboBox.addItem(category[0])

            cursor.execute("SELECT Наименование FROM Material")
            materials = cursor.fetchall()
            self.ui.comboBox_2.clear()
            for material in materials:
                self.ui.comboBox_2.addItem(material[0])

        except sqlite3.Error as e:
            print("Ошибка при извлечении данных из БД:", e)

    def display_image(self, image_path):
        try:
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                print("Изображение пусто или не удалось загрузить.")
            else:
                scaled_pixmap = pixmap.scaled(self.ui.Photo.size(), QtCore.Qt.KeepAspectRatio)
                self.ui.Photo.setPixmap(scaled_pixmap)
        except Exception as e:
            print("Ошибка при отображении изображения:", e)

    def browse_image(self, event):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.jpg *.jpeg)",
                                                   options=options)
        if file_path:
            self.ui.lineEdit_3.setText(os.path.basename(file_path))
            self.display_image(file_path)

    def save_changes(self):
        image_path = self.ui.lineEdit_3.text()
        value1 = image_path
        value2 = self.ui.lineEdit.text()
        value3 = self.ui.lineEdit_2.text()
        value4 = self.ui.comboBox.currentText()
        value5 = self.ui.lineEdit_4.text()
        value6 = self.ui.lineEdit_5.text()
        value7 = self.ui.lineEdit_6.text()
        value8 = self.ui.comboBox_2.currentText()

        if not all([value1, value2, value3, value4, value5, value6, value7, value8]):
            QMessageBox.warning(self, "Предупреждение", "Заполните все поля!")
            return

        try:
            cursor.execute("SELECT COUNT(*) FROM Tovar WHERE Артикул = ?", (value2,))
            exists = cursor.fetchone()[0]

            if exists > 0:
                QMessageBox.warning(self, "Предупреждение", "Товар с этим артикулом уже существует.")
            else:
                cursor.execute("INSERT INTO Tovar (Фото, Артикул, Наименование, Категория, Вес, Цена, Количество, Материал) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                               (value1, value2, value3, value4, value5, value6, value7, value8))
                db.commit()
                QMessageBox.information(self, "Информация", "Товар успешно добавлен.")
                print("Данные успешно добавлены в БД")
                self.parent().update_table()
        except sqlite3.Error as e:
            print("Ошибка при вставке данных в БД:", e)

        self.close()
class IzmenTovar(QDialog):
    def __init__(self, selected_tovar_articul, parent):
        super().__init__(parent)
        self.ui = Ui_Izmen_Tovar_Dialog()
        self.ui.setupUi(self)
        self.selected_tovar_articul = selected_tovar_articul.text()
        self.comboboxes()
        self.ui.lineEdit.setValidator(QIntValidator())
        self.ui.lineEdit_2.setValidator(QRegularExpressionValidator( QtCore.QRegularExpression("[а-яА-Я]*")))
        self.ui.lineEdit_4.setValidator(QDoubleValidator())
        self.ui.lineEdit_5.setValidator(QIntValidator())
        self.ui.lineEdit_6.setValidator(QIntValidator())
        self.load_tovar_data()
        self.ui.lineEdit_3.mousePressEvent = self.browse_image
        self.ui.pushButton1.clicked.connect(self.save_changes)
        self.ui.pushButton1_2.clicked.connect(self.delete_item)

    def load_tovar_data(self):
        try:
            cursor.execute("SELECT * FROM Tovar WHERE Артикул = ?", (self.selected_tovar_articul,))
            tovar = cursor.fetchone()
            if tovar:
                self.ui.lineEdit_3.setText(tovar[0])
                self.ui.lineEdit.setText(str(tovar[1]))
                self.ui.lineEdit_2.setText(tovar[2])
                self.ui.comboBox.setCurrentText(tovar[3])
                self.ui.lineEdit_4.setText(str(tovar[4]))
                self.ui.lineEdit_5.setText(str(tovar[5]))
                self.ui.lineEdit_6.setText(str(tovar[6]))
                self.ui.comboBox_2.setCurrentText(tovar[7])

        except sqlite3.Error as e:
            print("Ошибка при загрузке данных о товаре из БД:", e)

    def comboboxes(self):
        try:
            cursor.execute("SELECT Наименование FROM Category")
            categories = cursor.fetchall()
            self.ui.comboBox.clear()
            for category in categories:
                self.ui.comboBox.addItem(category[0])

            cursor.execute("SELECT Наименование FROM Material")
            materials = cursor.fetchall()
            self.ui.comboBox_2.clear()
            for material in materials:
                self.ui.comboBox_2.addItem(material[0])

        except sqlite3.Error as e:
            print("Ошибка при извлечении данных из БД:", e)
    def browse_image(self, event):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.jpg *.jpeg)",
                                                   options=options)
        if file_path:
            self.ui.lineEdit_3.setText(os.path.basename(file_path))

    def delete_item(self):
        try:
            reply = QMessageBox.question(self, 'Удаление товара', 'Вы точно хотите удалить товар?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                cursor.execute("DELETE FROM Tovar WHERE Артикул = ?", (int(self.selected_tovar_articul),))
                db.commit()
                QMessageBox.information(self, "Информация", "Товар успешно удален.")
                print("Товар успешно удален из БД")

                self.parent().update_table()
                self.close()

        except sqlite3.Error as e:
            print("Ошибка при удалении товара из БД:", e)

    def save_changes(self):
        image_path = self.ui.lineEdit_3.text()
        value2 = self.ui.lineEdit.text()
        value3 = self.ui.lineEdit_2.text()
        value4 = self.ui.comboBox.currentText()
        value5 = self.ui.lineEdit_4.text()
        value6 = self.ui.lineEdit_5.text()
        value7 = self.ui.lineEdit_6.text()
        value8 = self.ui.comboBox_2.currentText()
        #print((image_path, int(value2), value3, value4, value5, int(value6), int(value7), value8, int(self.selected_tovar_articul)))

        if not all([image_path, value2, value3, value4, value5, value6, value7, value8]):
            QMessageBox.warning(self, "Предупреждение", "Все поля должны быть заполнены")
            return
        try:

            cursor.execute("""
                UPDATE Tovar
                SET Фото = ?, Артикул = ?, Наименование = ?, Категория = ?, Вес = ?, Цена = ?, Количество = ?, Материал = ?
                WHERE Артикул = ?
            """, (image_path, int(value2), value3, value4, value5, int(value6), int(value7), value8, int(self.selected_tovar_articul)))

            db.commit()
            QMessageBox.information(self, "Информация", "Товар успешно изменен.")
            print("Данные успешно обновлены в БД")

            self.parent().update_table()
        except sqlite3.Error as e:
            print("Ошибка при обновлении данных в БД:", e)

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())