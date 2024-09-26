from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QLabel, QFileDialog, QDateTimeEdit,QComboBox, QSpinBox, QWidget, QVBoxLayout, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtCore
from PyQt5.QtCore import QDateTime
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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QImage, QPixmap
import io
import os
import sys
import sqlite3
from datetime import datetime, timedelta

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
        self.ui.tableWidget.setColumnWidth(5, 120)
        self.ui.tableWidget.setColumnWidth(6, 100)

        default_row_height = 90
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(default_row_height)

        self.ui.tableWidget.setFont(QFont("Arial", 12))

        for i in range(len(data)):
            for j in range(len(data[i])-1):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

        for i in range(len(data)):
            image_label = QLabel()
            image_path = data[i][0]
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(100, 100)
            image_label.setPixmap(pixmap)
            self.ui.tableWidget.setCellWidget(i, 0, image_label)

            for j in range(len(data[i]) - 1):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

    def set_selected_category(self, category):
        self.selected_category = category
        self.update_table()



    def show_sale(self):
        dialog = Sale()
        dialog.exec_()

    def show_otchet(self):
        dialog = Otchet()
        dialog.exec_()


    def show_suppliers(self):
        dialog = Suppliers()
        dialog.exec_()


    def show_category(self):
        dialog = Category()
        dialog.setParent(self)
        dialog.exec_()

    def show_dob_tovar(self):
        dialog = DobTovar(self)
        dialog.exec_()

    def show_izmen_tovar(self):
        dialog = IzmenTovar()
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

                # Преобразуем выбранный период времени в соответствующий формат даты
                if selected_time_period == "за последний месяц":
                    start_date = datetime.now() - timedelta(days=30)
                elif selected_time_period == "за последние 3 месяца":
                    start_date = datetime.now() - timedelta(days=90)
                elif selected_time_period == "за последние 6 месяцев":
                    start_date = datetime.now() - timedelta(days=180)
                else:
                    start_date = datetime.now() - timedelta(days=30)  # По умолчанию последний месяц

                # Формируем запрос к базе данных с учетом выбранного периода времени и категории
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

                # Отображаем график в graphicsView
                self.show_chart_in_graphics_view(selected_chart_type, sales_data)

        except Exception as e:
            print("Ошибка при формировании отчета:", e)

    def show_chart_in_graphics_view(self, selected_chart_type, sales_data):
        # Создаем виджет для отображения графика
        scene = QGraphicsScene()

        # Отображение графика
        pixmap = self.get_pixmap_from_matplotlib(selected_chart_type, sales_data)

        # Отображаем график в graphicsView
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

        # Получаем изображение из Matplotlib
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

        # Сохраняем график как временное изображение
        temp_path = 'temporary_graph.png'
        plt.savefig(temp_path)
        plt.close()  # Закрываем рисунок, чтобы он не отображался

        return temp_path

    def show_pie_chart(self, sales_data):
        categories = [data[1] for data in sales_data]
        revenue = [data[0] for data in sales_data]

        plt.figure(figsize=(8, 8))
        plt.pie(revenue, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Доля выручки по категориям товаров')

        # Сохраняем график как временное изображение
        temp_path = 'temporary_graph.png'
        plt.savefig(temp_path)
        plt.close()  # Закрываем рисунок, чтобы он не отображался

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

        # Сохраняем график как временное изображение
        temp_path = 'temporary_graph.png'
        plt.savefig(temp_path)
        plt.close()  # Закрываем рисунок, чтобы он не отображался

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

            # Добавление значений в comboBox
            self.ui.pushButton4.clicked.connect(self.huy)
            self.fill_time_period()
            self.fill_categories()
            self.fill_chart_types()


        except Exception as e:
            print("Ошибка в инициализации Sfor_otchet:", e)
    def huy(self):
        self.accept()
    def fill_time_period(self):
        try:
            # Добавление значений в comboBox для периода времени
            time_periods = ["за последний месяц", "за последние 3 месяца", "за последние 6 месяцев"]
            self.ui.comboBox.addItems(time_periods)

        except Exception as e:
            print("Ошибка при заполнении периода времени:", e)

    def fill_categories(self):
        try:
            # Получение категорий из БД (предполагается, что у вас есть соединение с БД и курсор)
            categories = self.get_categories_from_database()  # Функция, получающая категории из БД
            if categories:
                self.ui.comboBox_2.addItems(categories)
            zalupa = ["Выбрать все"]
            self.ui.comboBox_2.addItems(zalupa)

        except Exception as e:
            print("Ошибка при заполнении категорий:", e)

    def fill_chart_types(self):
        try:
            # Добавление видов диаграммы в comboBox_3
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

    def show_izmen_sale(self):
        dialog = Izmen_Sale()
        dialog.exec_()

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

            # Добавление поля для ввода количества
            quantity_label = QLabel(f"Количество товара {len(self.article_data) + 1}: ")
            quantity_input = QSpinBox()
            quantity_input.setMinimum(1)

            # Добавление в макет
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
            # Объединяем артикулы через запятую
            articles = ', '.join(item['combo'].currentText() for item in self.article_data)

            query = "INSERT INTO Sale (Номер_продажи, Сумма, Дата, Артикул, Количество_проданных_товаров) VALUES (?, ?, ?, ?, ?)"
            values = (sale_number, total_amount, sale_datetime, articles, total_quantity)
            self.cursor.execute(query, values)
        except Exception as e:
            print("Ошибка при выполнении запроса:", e)

        self.db.commit()
        self.close()
        self.parent_window.update_table_sale()

class Izmen_Sale(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Izmen_Sale_Dialog()
        self.ui.setupUi(self)

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

    def show_izmen_sapp(self):
        dialog = IzmenSup()
        dialog.exec_()

class DobSup(QDialog):
    def __init__(self, db_connection):
        super().__init__()
        self.ui = Ui_Dob_Sup_Dialog()
        self.ui.setupUi(self)
        self.db_connection = db_connection

        self.ui.pushButton1_3.clicked.connect(self.add_new_combo_box)
        self.ui.pushButton1.clicked.connect(self.save_changes_sup)

        # Список для хранения всех ComboBox
        self.combo_boxes = []

    def add_new_combo_box(self):
        new_combo_box = QComboBox()
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Артикул FROM Tovar")
        articles = cursor.fetchall()
        for article in articles:
            new_combo_box.addItem(str(article[0]))

        self.combo_boxes.append(new_combo_box)
        self.ui.verticalLayout.addWidget(new_combo_box)

    def save_changes_sup(self):
        value_1 = self.ui.lineEdit.text()
        value_2 = self.ui.lineEdit_2.text()
        value_3 = int(self.ui.lineEdit_3.text())

        selected_articles = []
        for combo_box in self.combo_boxes:
            selected_articles.append(combo_box.currentText())

        articles_string = ', '.join(selected_articles)

        cursor = self.db_connection.cursor()
        cursor.execute(
            "INSERT INTO Suppliers (ФИО, Наименование_организации, Контактная_информация, Товары) VALUES (?, ?, ?, ?)",
            (value_1, value_2, value_3, articles_string))
        self.db_connection.commit()
        self.accept()

class IzmenSup(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Izmen_Sup_Dialog()
        self.ui.setupUi(self)

class DobCategory(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dob_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton1_2.clicked.connect(self.save_changes_category)

    def save_changes_category(self):
        value1 = self.ui.lineEdit.text()

        try:
            cursor.execute(
                "INSERT INTO Category (Наименование) VALUES (?)",
                (value1,))
            db.commit()
            print("Данные успешно добавлены в БД")
        except sqlite3.Error as e:
            print("Ошибка при вставке данных в БД:", e)

        self.close()


class IzmenCategory(QDialog):
    def __init__(self, selected_category, load_categories_func, parent=None):
        super().__init__(parent)
        self.ui = Ui_Izmen_Dialog()
        self.ui.setupUi(self)
        self.selected_category = selected_category
        self.load_categories = load_categories_func  # Сохраняем функцию загрузки категорий
        self.ui.lineEdit.setText(selected_category)
        self.ui.pushButton1_2.clicked.connect(self.save_changes)
        self.ui.pushButton1_3.clicked.connect(self.delete_category)

    def save_changes(self):
        new_category_name = self.ui.lineEdit.text()
        try:
            cursor.execute("UPDATE Category SET Наименование = ? WHERE Наименование = ?",
                           (new_category_name, self.selected_category))
            db.commit()
            print("Category updated successfully in the database")
            self.load_categories()  # Обновляем список категорий, вызывая переданную функцию
            self.accept()
        except sqlite3.Error as e:
            print("Ошибка при обновлении данных в БД:", e)

    def delete_category(self):
        try:
            selected_category = self.selected_category
            print("Trying to delete category:", selected_category)  # Отладочный вывод
            cursor.execute("DELETE FROM Category WHERE UPPER(Наименование) = UPPER(?)", (selected_category,))
            db.commit()
            print("Category deleted successfully from the database")  # Отладочный вывод
            self.load_categories()  # Обновляем список категорий в приложении
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

        # Проходим по элементам в listWidget и ищем совпадения
        for index in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(index)
            if item.text().lower().startswith(input_text):
                self.ui.listWidget.setCurrentItem(item)  # текущий элемент
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
        self.parent().set_selected_category(selected_category)
        self.hide()

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
        main_window = self.parent()
        if main_window:
            main_window.set_selected_category(selected_category)
        self.accept()

    def reset_filter(self):
        self.ui.lineEdit.clear()
        self.ui.listWidget.setCurrentRow(-1)
        self.parent().set_selected_category(None)
    def show_dob_category(self):
        dialog = DobCategory()
        dialog.exec_()

    def show_izmen_category(self):
        selected_category = self.ui.listWidget.currentItem().text()
        if selected_category:
            dialog = IzmenCategory(selected_category, self.load_categories, self)
            dialog.exec_()

class DobTovar(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Dob_Tovar_Dialog()
        self.ui.setupUi(self)
        self.comboboxes()
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
            self.ui.lineEdit_3.setText(os.path.basename(file_path))  # Используйте только имя файла
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

        try:
            cursor.execute(
                "INSERT INTO Tovar (Фото, Артикул, Наименование, Категория, Вес, Цена, Количество, Материал) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (value1, value2, value3, value4, value5, value6, value7, value8))
            db.commit()
            print("Данные успешно добавлены в БД")

            self.parent().update_table()  # Обновляем таблицу после вставки новых данных
        except sqlite3.Error as e:
            print("Ошибка при вставке данных в БД:", e)

        self.close()
class IzmenTovar(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Izmen_Tovar_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())