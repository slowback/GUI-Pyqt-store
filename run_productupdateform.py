from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtGui
from module_product import *
import productupdateform
import sys


class MyApp(QMainWindow):
    idx = 0

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = productupdateform.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        self.ui.pushButton.clicked.connect(self.getpic)
        self.ui.listWidget_2.itemSelectionChanged.connect(self.show_p_data)
        self.get_p_data()

    def get_p_data(self):
        data = select_all_product(0)
        self.ui.listWidget_2.clear()
        count = 1
        for row in data:
            if count > 3:
                if count < len(data) - 3:
                    self.ui.listWidget_2.insertItem(count, str(row))
            count = count + 1
        self.ui.listWidget_2.setCurrentRow(MyApp.idx)

    def getpic(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", "pic/")
        # TODO: show filename
        print("filename: ", filename)

        filename = filename[0]
        start = filename.find("pic/", 1) + 4
        stop = len(filename)
        picname = filename[start:stop]
        self.ui.lineEdit.setText(picname)
        self.ui.label_8.setPixmap(QtGui.QPixmap(filename))
        # self.ui.label_8.adjustSize()

    def show_p_data(self):
        msg = ""
        data = self.ui.listWidget_2.selectedItems()
        for row in data:
            msg = row.text()

        data = msg.split(" ", 6)
        data0 = data[0][1 : len(data[0]) - 1]
        data1 = data[1][1 : len(data[1]) - 1]
        data2 = data[2][1 : len(data[2]) - 1].replace(",", "")
        data3 = data[3][1 : len(data[3]) - 1]
        data4 = data[4][1 : len(data[4]) - 1]
        filename = "pic/" + data4
        self.ui.label_8.setPixmap(QtGui.QPixmap(filename))
        self.ui.lineEdit.setText(data4)
        self.ui.label_6.setText(data0)
        self.ui.lineEdit_3.setText(data1)
        self.ui.lineEdit_2.setText(data2)
        self.ui.lineEdit_4.setText(data3)

    def save_data(self):
        pid = self.ui.label_6.text()
        pname = self.ui.lineEdit_3.text()
        pqty = self.ui.lineEdit_2.text()
        pcost = self.ui.lineEdit_4.text()
        ppic = self.ui.lineEdit.text()
        update_product(pid, pname, pqty, pcost, ppic)
        QMessageBox.information(self, "info", "Data Updated")
        MyApp.idx = self.ui.listWidget_2.currentRow()
        self.close()
        MyApp(self).show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
