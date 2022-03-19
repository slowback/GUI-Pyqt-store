from tracemalloc import stop
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5 import QtGui, QtCore
from module_product import *
import sys
import productinsertform


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = productinsertform.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        self.ui.pushButton.clicked.connect(self.getpic)
        self.get_p_data()

    def get_p_data(self):
        data = select_last_product()
        # TODO: print show data
        print("data: ", data)
        pid = 0
        if data != 0:
            pid = str(data)[1:]
        pid = str(int(pid) + 1)
        if len(pid) == 1:
            pid = "P00" + pid
        if len(pid) == 2:
            pid = "Po" + pid
        if len(pid) == 3:
            pid = "P" + pid
        self.ui.label_6.setText(pid)
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_4.clear()
        self.ui.label_7.setPixmap(QtGui.QPixmap("None"))
        self.ui.label_7.setText("Picture File")
        self.ui.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.lineEdit_3.setFocus()

    def getpic(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", "pic/")
        filename = filename[0]
        start = filename.find("pic/", 1) + 4
        stop = len(filename)
        picname = filename[start:stop]
        self.ui.lineEdit.setText(picname)
        self.ui.label_7.setPixmap(QtGui.QPixmap(filename))
        # self.ui.label_7.adjustSize()

    def save_data(self):
        pid = self.ui.label_6.text()
        pname = self.ui.lineEdit_3.text()
        qtyA = self.ui.lineEdit_2.text()
        pcost = self.ui.lineEdit_4.text()
        ppic = self.ui.lineEdit.text()
        insert_product(pid, pname, qtyA, pcost, ppic)
        QMessageBox.information(self, "info", "Data Inserted")
        self.get_p_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
