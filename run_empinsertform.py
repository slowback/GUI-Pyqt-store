from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
import sys
import employeeinsertform
from module_emp import insert_employee, select_all_employee, select_last_employee_id
import random


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = employeeinsertform.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        self.get_emp_data()

    def get_emp_data(self):
        data = select_last_employee_id()
        # TODO show data
        print("data: ", data)
        empid = 0
        if data != 0:
            empid = str(data)[1:]

        empid = str(int(empid) + 1)
        # TODO print empid
        print("empid: ", empid)

        if len(empid) == 1:
            empid = "E00" + empid
        if len(empid) == 2:
            empid = "E0" + empid
        if len(empid) == 3:
            empid = "E" + empid

        self.ui.lineEdit.setText(empid)
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem("admin")
        self.ui.comboBox.addItem("user")
        self.ui.comboBox.currentText = "admin"
        pw = random.randrange(1000, 9999)
        self.ui.lineEdit_2.setText(str(pw))

    def save_data(self):
        empid = self.ui.lineEdit.text()
        emppw = self.ui.lineEdit_2.text()
        emptype = self.ui.comboBox.currentIndex() + 1
        insert_employee(empid, emppw, emptype)
        QMessageBox.information(self, "info", "Data Inserted")
        data = select_all_employee(1)
        if len(data) > 8:
            self.get_emp_data()
        else:
            QMessageBox.information(self, "info", f"login data is {empid}; {emppw}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
