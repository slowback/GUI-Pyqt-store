from itertools import product
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import menusform
import run_productinsertform
import run_productupdateform
import run_productqryform
import run_stockininsertform
import run_stockinqryform
import run_empinsertform
import run_empqryform
import run_empupdateform
import sys


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = menusform.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_7.clicked.connect(self.exits)
        self.ui.pushButton.clicked.connect(self.get_empinsert_form)
        self.ui.pushButton_2.clicked.connect(self.get_productinsert_form)
        self.ui.pushButton_3.clicked.connect(self.get_stockinsert_form)
        self.ui.pushButton_4.clicked.connect(self.get_empqry_form)
        self.ui.pushButton_5.clicked.connect(self.get_productqry_form)
        self.ui.pushButton_6.clicked.connect(self.get_stockinqry_form)
        self.ui.actionproduct.triggered.connect(self.get_productupdate_form)
        self.ui.actionemployee.triggered.connect(self.get_empupdate_form)

    def get_windowtitle(self):
        empid = MyApp.windowTitle(self)
        print("empid: ", empid)
        empid = empid.split(" by ", 2)
        return empid[1]

    def get_empinsert_form(self):
        empinsert_app = run_empinsertform.MyApp(self)
        empinsert_app.show()

    def get_empqry_form(self):
        empqry_app = run_empqryform.MyApp(self)
        empqry_app.show()

    def get_productinsert_form(self):
        productinsert_app = run_productinsertform.MyApp(self)
        productinsert_app.show()

    def get_productqry_form(self):
        productqry_app = run_productqryform.MyApp(self)
        productqry_app.show()

    def get_stockinsert_form(self):
        stockinsert_app = run_stockininsertform.MyApp(self)
        empid = self.get_windowtitle()
        stockinsert_app.ui.label_2.setText(empid)
        stockinsert_app.show()

    def get_stockinqry_form(self):
        stockinqry_app = run_stockinqryform.MyApp(self)
        stockinqry_app.show()

    def get_productupdate_form(self):
        productupdate_qpp = run_productupdateform.MyApp(self)
        productupdate_qpp.show()

    def get_empupdate_form(self):
        empupdate_app = run_empupdateform.MyApp(self)
        empupdate_app.show()

    @staticmethod
    def exits():
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
