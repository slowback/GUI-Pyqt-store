from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore
from module_product import *
from module_stockin import *
import stockininsertform
import sys


class MyApp(QMainWindow):
    idx = 0
    ppic = ""
    empid = ""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = stockininsertform.Ui_Stockinforminsert()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        self.ui.listWidget.itemSelectionChanged.connect(self.show_p_data)
        self.get_st_date()
        self.get_p_data()

    def get_st_date(self):
        if self.ui.label_2.setText(MyApp.empid) == "":
            self.ui.label_2.setText(MyApp.empid)
        self.ui.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

    def get_p_data(self):
        data = select_all_product(0)
        self.ui.listWidget.clear()
        count = 1

        for row in data:
            if count > 3:
                if count < len(data) - 3:
                    self.ui.listWidget.insertItem(count, str(row))
            count += 1
        self.ui.listWidget.setCurrentRow(MyApp.idx)

    def show_p_data(self):
        data = self.ui.listWidget.selectedItems()
        msg = ""
        for row in data:
            msg = row.text()

        data = msg.split(" ", 5)
        data0 = data[0][1 : len(data[0]) - 1]
        data1 = data[1][1 : len(data[1]) - 1]
        data2 = data[2][1 : len(data[2]) - 1].replace(",", "")
        data3 = data[3][1 : len(data[3]) - 1]
        data4 = data[4][1 : len(data[4]) - 1]

        MyApp.ppic = data4
        self.ui.label_6.setText(data0)
        self.ui.label_9.setText(data1)
        self.ui.label_11.setText(str(data2))
        self.ui.label_12.setText(str(data3))
        self.ui.lineEdit.setFocus()

    def save_data(self):
        MyApp.empid = self.ui.label_2.text()
        indate = self.ui.dateEdit.text()
        pid = self.ui.label_6.text()
        pname = self.ui.label_9.text()
        pqty = int(self.ui.label_11.text().replace(",", ""))
        pcost = float(self.ui.label_12.text().replace(",", ""))

        stqty = int(self.ui.lineEdit.text().replace(",", ""))
        stcost = float(self.ui.lineEdit_2.text().replace(",", ""))

        newcost = (pqty * pcost) + (stqty * stcost) / (pqty + stqty)
        pqty = pqty + stqty

        insert_stockin(indate, pid, MyApp.empid, stqty, stcost)
        update_product(pid, pname, pqty, newcost, MyApp.ppic)
        QMessageBox.information(self, "info", "Data Inserted")
        MyApp.idx = self.ui.listWidget.currentRow()
        self.close()
        MyApp(self).show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
