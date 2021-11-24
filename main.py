import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from PyQt5 import uic

HEADER = ["ID", "Название сорта", "Степень обжарки", "Молотый",
          "Описание вкуса", "Цена", "Объем упаковки"]


class CoffeeWindow(QMainWindow):

    def __init__(self, database):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.database = database
        self.initUi()

    def initUi(self):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            results = cursor.execute("SELECT * FROM sorts").fetchall()
        self.coffee_table.setColumnCount(len(HEADER))
        self.coffee_table.setHorizontalHeaderLabels(HEADER)
        self.coffee_table.setRowCount(len(results))
        self.coffee_table.resizeColumnsToContents()
        for i, row in enumerate(results):
            for j, elem in enumerate(row):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeWindow("coffee.db")
    window.show()
    sys.exit(app.exec())
