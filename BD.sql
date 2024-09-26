--
-- File generated with SQLiteStudio v3.4.4 on �� ��� 16 15:51:43 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Category
CREATE TABLE IF NOT EXISTS Category (������������ TEXT (50) PRIMARY KEY NOT NULL);
INSERT INTO Category (������������) VALUES ('������� �������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('������ ��������');
INSERT INTO Category (������������) VALUES ('������');
INSERT INTO Category (������������) VALUES ('������');
INSERT INTO Category (������������) VALUES ('������� ������');
INSERT INTO Category (������������) VALUES ('������-�����');
INSERT INTO Category (������������) VALUES ('������-������');
INSERT INTO Category (������������) VALUES ('�������� � ������������ �������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('����-��������');
INSERT INTO Category (������������) VALUES ('������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('��������� ��������');
INSERT INTO Category (������������) VALUES ('��������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('����������� ������');
INSERT INTO Category (������������) VALUES ('����������� ������');
INSERT INTO Category (������������) VALUES ('����������� ������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('�����');
INSERT INTO Category (������������) VALUES ('������� �������');
INSERT INTO Category (������������) VALUES ('������� ������');
INSERT INTO Category (������������) VALUES ('������� ��������');
INSERT INTO Category (������������) VALUES ('������� ��������');
INSERT INTO Category (������������) VALUES ('������� ������');
INSERT INTO Category (������������) VALUES ('������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('��������');
INSERT INTO Category (������������) VALUES ('��������� � ����');
INSERT INTO Category (������������) VALUES ('���������');
INSERT INTO Category (������������) VALUES ('������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('�������');
INSERT INTO Category (������������) VALUES ('������� �������� ����');
INSERT INTO Category (������������) VALUES ('������� �������� ����');
INSERT INTO Category (������������) VALUES ('����� ��������');
INSERT INTO Category (������������) VALUES ('������� ��������');
INSERT INTO Category (������������) VALUES ('������ ��������');
INSERT INTO Category (������������) VALUES ('����� - �����');

-- Table: Material
CREATE TABLE IF NOT EXISTS Material (������������ TEXT (150) PRIMARY KEY NOT NULL);
INSERT INTO Material (������������) VALUES (' ������������ ��������');
INSERT INTO Material (������������) VALUES ('����������� �����');
INSERT INTO Material (������������) VALUES ('�����');
INSERT INTO Material (������������) VALUES ('�������');
INSERT INTO Material (������������) VALUES ('�������');
INSERT INTO Material (������������) VALUES ('������� ������');
INSERT INTO Material (������������) VALUES ('������� ������');
INSERT INTO Material (������������) VALUES ('����� ������');
INSERT INTO Material (������������) VALUES ('������ ������');
INSERT INTO Material (������������) VALUES ('������� ������ � ������������');
INSERT INTO Material (������������) VALUES ('������ � ������������');
INSERT INTO Material (������������) VALUES ('����� ������ � ������������');
INSERT INTO Material (������������) VALUES ('������� ������ � ��������');
INSERT INTO Material (������������) VALUES ('������ � ���������');
INSERT INTO Material (������������) VALUES ('������� � ������������');
INSERT INTO Material (������������) VALUES ('������� � ����������');
INSERT INTO Material (������������) VALUES ('������� � ��������');
INSERT INTO Material (������������) VALUES ('������� � ��������');
INSERT INTO Material (������������) VALUES ('������ � ��������');

-- Table: Sale
CREATE TABLE IF NOT EXISTS Sale ("����� �������" INTEGER PRIMARY KEY NOT NULL, ����� REAL NOT NULL, ���� TEXT NOT NULL, ������� INTEGER REFERENCES Tovar (�������) ON DELETE CASCADE ON UPDATE CASCADE NOT NULL, "���������� ��������� �������" INTEGER NOT NULL);
INSERT INTO Sale ("����� �������", �����, ����, �������, "���������� ��������� �������") VALUES (1, '9 430', '02.10.2023', 1111, 1);
INSERT INTO Sale ("����� �������", �����, ����, �������, "���������� ��������� �������") VALUES (2, '4 370', '03.10.2023', 1115, 1);

-- Table: Sappliers
CREATE TABLE IF NOT EXISTS Sappliers (��� TEXT (150) NOT NULL, "������������ �����������" TEXT (70) PRIMARY KEY NOT NULL, ������ INTEGER (10) NOT NULL REFERENCES Tovar (�������) ON DELETE CASCADE ON UPDATE CASCADE, "���������� ����������" INTEGER (50) NOT NULL);
INSERT INTO Sappliers (���, "������������ �����������", ������, "���������� ����������") VALUES ('������ ���� ��������', '��� ������', 1115, 89087698876);
INSERT INTO Sappliers (���, "������������ �����������", ������, "���������� ����������") VALUES ('������ ������� ����������', '�� ������� ������� ����������', 1113, 79678048870);
INSERT INTO Sappliers (���, "������������ �����������", ������, "���������� ����������") VALUES ('�������� ������ ���������', '������������� ��������', 1112, 8007076759);
INSERT INTO Sappliers (���, "������������ �����������", ������, "���������� ����������") VALUES ('����� ����� ���������', 'JWSOTI', 1111, 79939155449);

-- Table: Tovar
CREATE TABLE IF NOT EXISTS Tovar (���� BLOB, ������� INTEGER PRIMARY KEY NOT NULL, ������������ TEXT (100) NOT NULL, ��������� TEXT (50) NOT NULL REFERENCES Category (������������) ON DELETE CASCADE ON UPDATE CASCADE, ��� REAL NOT NULL, ���� NUMERIC NOT NULL, ���������� INTEGER (20) NOT NULL, �������� TEXT (150) NOT NULL REFERENCES Material (������������) ON DELETE CASCADE ON UPDATE CASCADE);
INSERT INTO Tovar (����, �������, ������������, ���������, ���, ����, ����������, ��������) VALUES (NULL, 1111, '������ �� ������ �� ������� "Love"', '������', 0.82, '9 430', 2, '������ ������');
INSERT INTO Tovar (����, �������, ������������, ���������, ���, ����, ����������, ��������) VALUES (NULL, 1112, '������ �� ������� � ��������', '������ ��������', 1.51, '1 706', 4, '������� � ��������');
INSERT INTO Tovar (����, �������, ������������, ���������, ���, ����, ����������, ��������) VALUES (NULL, 1113, '������ �� ������� � ��������', '������', 1.61, '4 870', 5, '������� � ��������');
INSERT INTO Tovar (����, �������, ������������, ���������, ���, ����, ����������, ��������) VALUES (NULL, 1114, '�����-����� �� ������� � �������� ���������', '����� - �����', 9.8, '31 944', 3, '������ � ��������');
INSERT INTO Tovar (����, �������, ������������, ���������, ���, ����, ����������, ��������) VALUES (NULL, 1115, '�������� �� ������ "������"', '��������', 0.36, '4 370', 6, '������ ������');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
