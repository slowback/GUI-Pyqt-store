from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from module_product import *
import productqryform
import sys


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = productqryform.Ui_Form()
        self.ui.setupUi(self)
        self.ui.close.clicked.connect(self.close)
        self.load_data()

    def load_data(self):
        data = select_all_product(1)
        msg = print_product_qry(data)
        self.ui.showlist.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
