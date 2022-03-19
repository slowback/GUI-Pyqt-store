from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
import sys
import employeeupdateform
from module_emp import delete_employee, select_all_employee, update_employee


class MyApp(QMainWindow):
    idx = 0
    active = 1

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = employeeupdateform.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        self.ui.listWidget.itemSelectionChanged.connect(self.show_emp_data)
        self.ui.listWidget.doubleClicked.connect(self.delete_data)
        self.get_emp_data()

    def get_emp_data(self):
        data = select_all_employee(0)
        self.ui.listWidget.clear()
        count = 1
        for row in data:
            if count > 3:
                if count < len(data) - 3:
                    self.ui.listWidget.insertItem(count, str(row))
            count += 1
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem("admin")
        self.ui.comboBox.addItem("user")
        self.ui.listWidget.setCurrentRow(MyApp.idx)

    def show_emp_data(self):
        msg = ""
        data = self.ui.listWidget.selectedItems()
        for row in data:
            msg = row.text()

        data = msg.split(" ", 4)

        # TODO: you should delete when finished.
        print("data:", data)

        data0 = data[0][1 : len(data[0]) - 1]
        data1 = data[1][1 : len(data[1]) - 1]
        data2 = data[2][1 : len(data[2]) - 1]

        # TODO: you should delete when finished.
        print("data0: ", data0)
        print("data1: ", data1)
        print("data2: ", data2)

        MyApp.active = data[3][1 : len(data[3]) - 1]

        self.ui.label_8.setText(data0)
        self.ui.lineEdit_2.setText(data1)
        self.ui.comboBox.setCurrentText(data2)

    def delete_data(self):
        empid = self.ui.label_8.text()

        if MyApp.active == "active":
            msg = "Delete "
            active = 1
        else:
            msg = "Delete inactive "
            active = 0

        resp = QMessageBox.question(
            self,
            "confirm",
            msg + "Data ?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if resp == QMessageBox.Yes:
            delete_employee(empid, active)
            self.close()
            MyApp.idx = self.ui.listWidget.currentRow()
            MyApp(self).show()

    def save_data(self):
        empid = self.ui.label_8.text()
        emppw = self.ui.lineEdit_2.text()
        emptype = self.ui.comboBox.currentIndex()
        update_employee(empid, emppw, (emptype + 1))
        QMessageBox.information(self, "info", "Data Updated")
        self.close()
        MyApp.idx = self.ui.listWidget.currentRow()

        # TODO: you should delete when finished.
        print("MyApp.idx: ", MyApp.idx)
        MyApp(self).show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
