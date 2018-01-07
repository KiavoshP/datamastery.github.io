#!/usr/bin/env python3

import pymysql
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QGroupBox,
    QVBoxLayout,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QLabel,
    qApp,
    QAction,
    QSplitter,
    QListView,
    QTabWidget,
    QTableView
)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem
)
from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QVariant
)
from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlQuery,
    QSqlQueryModel
)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("MySQL Browser")
        self.create_menu_bar()
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.addWidget(self.create_db_list())
        self.splitter.addWidget(QLabel("Select a database from the list"))
        self.setCentralWidget(self.splitter)

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        self.create_file_menu(menu_bar)

    def create_file_menu(self, menu_bar):
        exit = QAction("Exit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip("Exit")
        exit.triggered.connect(qApp.quit)

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(exit)

    def create_db_list(self):
        self.list_view = QListView()
        self.list_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.list_model)
        cursor = connection.cursor()
        cursor.execute("show databases")
        for row in cursor:
            self.list_model.appendRow(QStandardItem(row['Database']))
        return self.list_view

class DbLoginDialog(QDialog):
    def __init__(self):
        super(DbLoginDialog, self).__init__()
        self.setModal(True)
        self.setWindowTitle("Login to MySQL Server")

        self.host = QLineEdit("localhost")
        self.user = QLineEdit("root")
        self.password = QLineEdit()

        form_group_box = QGroupBox("MySQL Server Login Credentials")
        layout = QFormLayout()
        layout.addRow(QLabel("Host:"), self.host)
        layout.addRow(QLabel("User:"), self.user)
        layout.addRow(QLabel("Password:"), self.password)
        form_group_box.setLayout(layout)

        # Consider these 3 lines boiler plate for a standard Ok | Cancel dialog
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(form_group_box)
        vbox_layout.addWidget(buttons)
        self.setLayout(vbox_layout)
        self.password.setFocus()

if __name__=='__main__':
    app = QApplication(sys.argv)
    login = DbLoginDialog()

    # This is how you check which button the user used to dismiss the dialog.
    if login.exec() == QDialog.Accepted:
        # connection is global so we can use it in any class, function, or method
        # defined in this module
        global connection
        try:
            connection = pymysql.connect(host=login.host.text(),
                                         user=login.user.text(),
                                         password=login.password.text(),
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
        except:
            print(f"Couldn't log {login.user.text()} in to MySQL server on {login.host.text()}")
            qApp.quit()
            sys.exit()
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())
    else:
        qApp.quit()
