--
-- File generated with SQLiteStudio v3.4.4 on Сб дек 16 15:51:43 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Category
CREATE TABLE IF NOT EXISTS Category (Наименование TEXT (50) PRIMARY KEY NOT NULL);
INSERT INTO Category (Наименование) VALUES ('Браслет Мужской');
INSERT INTO Category (Наименование) VALUES ('Браслет');
INSERT INTO Category (Наименование) VALUES ('Серьги Гвоздики');
INSERT INTO Category (Наименование) VALUES ('Серьги');
INSERT INTO Category (Наименование) VALUES ('Кольца');
INSERT INTO Category (Наименование) VALUES ('Носовые кольца');
INSERT INTO Category (Наименование) VALUES ('Серьги-каффы');
INSERT INTO Category (Наименование) VALUES ('Серьги-кольца');
INSERT INTO Category (Наименование) VALUES ('Браслеты с драгоценными камнями');
INSERT INTO Category (Наименование) VALUES ('Пуссеты');
INSERT INTO Category (Наименование) VALUES ('Шарм-браслеты');
INSERT INTO Category (Наименование) VALUES ('Чокеры');
INSERT INTO Category (Наименование) VALUES ('Цепочки');
INSERT INTO Category (Наименование) VALUES ('Жемчужные ожерелья');
INSERT INTO Category (Наименование) VALUES ('Ожерелья');
INSERT INTO Category (Наименование) VALUES ('Сигнеты');
INSERT INTO Category (Наименование) VALUES ('Коктейльные кольца');
INSERT INTO Category (Наименование) VALUES ('Помолвочные кольца');
INSERT INTO Category (Наименование) VALUES ('Обручальные кольца');
INSERT INTO Category (Наименование) VALUES ('Пирсинг');
INSERT INTO Category (Наименование) VALUES ('Колье');
INSERT INTO Category (Наименование) VALUES ('Браслет Женский');
INSERT INTO Category (Наименование) VALUES ('Детские кольца');
INSERT INTO Category (Наименование) VALUES ('Детские подвески');
INSERT INTO Category (Наименование) VALUES ('Детские браслеты');
INSERT INTO Category (Наименование) VALUES ('Детские серьги');
INSERT INTO Category (Наименование) VALUES ('Ободки');
INSERT INTO Category (Наименование) VALUES ('Заколки');
INSERT INTO Category (Наименование) VALUES ('Диадемы');
INSERT INTO Category (Наименование) VALUES ('Подвески');
INSERT INTO Category (Наименование) VALUES ('Медальоны с фото');
INSERT INTO Category (Наименование) VALUES ('Медальоны');
INSERT INTO Category (Наименование) VALUES ('Кулоны');
INSERT INTO Category (Наименование) VALUES ('Запонки');
INSERT INTO Category (Наименование) VALUES ('Перстни');
INSERT INTO Category (Наименование) VALUES ('Женские наручные часы');
INSERT INTO Category (Наименование) VALUES ('Мужские наручные часы');
INSERT INTO Category (Наименование) VALUES ('Ушные пирсинги');
INSERT INTO Category (Наименование) VALUES ('Бровные пирсинги');
INSERT INTO Category (Наименование) VALUES ('Губные пирсинги');
INSERT INTO Category (Наименование) VALUES ('Колье - чокер');

-- Table: Material
CREATE TABLE IF NOT EXISTS Material (Наименование TEXT (150) PRIMARY KEY NOT NULL);
INSERT INTO Material (Наименование) VALUES (' Родированное покрытие');
INSERT INTO Material (Наименование) VALUES ('Нержавеющая сталь');
INSERT INTO Material (Наименование) VALUES ('Титан');
INSERT INTO Material (Наименование) VALUES ('Платина');
INSERT INTO Material (Наименование) VALUES ('Серебро');
INSERT INTO Material (Наименование) VALUES ('Зеленое золото');
INSERT INTO Material (Наименование) VALUES ('Розовое золото');
INSERT INTO Material (Наименование) VALUES ('Белое золото');
INSERT INTO Material (Наименование) VALUES ('Желтое золото');
INSERT INTO Material (Наименование) VALUES ('Розовое золото с бриллиантами');
INSERT INTO Material (Наименование) VALUES ('Золото с бриллиантами');
INSERT INTO Material (Наименование) VALUES ('Белое золото с бриллиантами');
INSERT INTO Material (Наименование) VALUES ('Розовое золото с жемчугом');
INSERT INTO Material (Наименование) VALUES ('Золото с сапфирами');
INSERT INTO Material (Наименование) VALUES ('Платина с бриллиантами');
INSERT INTO Material (Наименование) VALUES ('Серебро с изумрудами');
INSERT INTO Material (Наименование) VALUES ('Серебро с жемчугом');
INSERT INTO Material (Наименование) VALUES ('Серебро с топазами');
INSERT INTO Material (Наименование) VALUES ('Золото с жемчугом');

-- Table: Sale
CREATE TABLE IF NOT EXISTS Sale ("Номер продажи" INTEGER PRIMARY KEY NOT NULL, Сумма REAL NOT NULL, Дата TEXT NOT NULL, Артикул INTEGER REFERENCES Tovar (Артикул) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, "Количество проданных товаров" INTEGER NOT NULL);
INSERT INTO Sale ("Номер продажи", Сумма, Дата, Артикул, "Количество проданных товаров") VALUES (1, '9 430', '02.10.2023', 1111, 1);
INSERT INTO Sale ("Номер продажи", Сумма, Дата, Артикул, "Количество проданных товаров") VALUES (2, '4 370', '03.10.2023', 1115, 1);

-- Table: Sappliers
CREATE TABLE IF NOT EXISTS Sappliers (ФИО TEXT (150) NOT NULL, "Наименование организации" TEXT (70) PRIMARY KEY NOT NULL, Товары INTEGER (10) NOT NULL REFERENCES Tovar (Артикул) ON DELETE CASCADE ON UPDATE CASCADE, "Контактная информация" INTEGER (50) NOT NULL);
INSERT INTO Sappliers (ФИО, "Наименование организации", Товары, "Контактная информация") VALUES ('Иванов Иван Иванович', 'РПК Ремарк', 1115, 89087698876);
INSERT INTO Sappliers (ФИО, "Наименование организации", Товары, "Контактная информация") VALUES ('Покров Виталий Викторович', 'ИП Покрова Виталий Викторович', 1113, 79678048870);
INSERT INTO Sappliers (ФИО, "Наименование организации", Товары, "Контактная информация") VALUES ('Борисова Лариса Караваева', 'Кольчугинский мельхиор', 1112, 8007076759);
INSERT INTO Sappliers (ФИО, "Наименование организации", Товары, "Контактная информация") VALUES ('Жилов Михил Антонович', 'JWSOTI', 1111, 79939155449);

-- Table: Tovar
CREATE TABLE IF NOT EXISTS Tovar (Фото BLOB, Артикул INTEGER PRIMARY KEY NOT NULL, Наименование TEXT (100) NOT NULL, Категория TEXT (50) NOT NULL REFERENCES Category (Наименование) ON DELETE CASCADE ON UPDATE CASCADE, Вес REAL NOT NULL, Цена NUMERIC NOT NULL, Количество INTEGER (20) NOT NULL, Материал TEXT (150) NOT NULL REFERENCES Material (Наименование) ON DELETE CASCADE ON UPDATE CASCADE);
INSERT INTO Tovar (Фото, Артикул, Наименование, Категория, Вес, Цена, Количество, Материал) VALUES (NULL, 1111, 'Кольцо из золота на фалангу "Love"', 'Кольца', 0.82, '9 430', 2, 'Желтое золото');
INSERT INTO Tovar (Фото, Артикул, Наименование, Категория, Вес, Цена, Количество, Материал) VALUES (NULL, 1112, 'Серьги из серебра с жемчугом', 'Серьги Гвоздики', 1.51, '1 706', 4, 'Серебро с жемчугом');
INSERT INTO Tovar (Фото, Артикул, Наименование, Категория, Вес, Цена, Количество, Материал) VALUES (NULL, 1113, 'Кольцо из серебра с топазами', 'Кольца', 1.61, '4 870', 5, 'Серебро с топазами');
INSERT INTO Tovar (Фото, Артикул, Наименование, Категория, Вес, Цена, Количество, Материал) VALUES (NULL, 1114, 'Колье-чокер из жемчуга с золотыми вставками', 'Колье - чокер', 9.8, '31 944', 3, 'Золото с жемчугом');
INSERT INTO Tovar (Фото, Артикул, Наименование, Категория, Вес, Цена, Количество, Материал) VALUES (NULL, 1115, 'Подвеска из золота "Корона"', 'Подвески', 0.36, '4 370', 6, 'Желтое золото');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
