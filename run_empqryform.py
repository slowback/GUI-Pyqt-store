from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import employeeqryform
from module_emp import *
import sys


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = employeeqryform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.close_2.clicked.connect(self.close)
        self.load_data()

    def load_data(self):
        data = select_all_employee(1)
        msg = print_emp_qry(data)
        self.ui.showlist_2.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
