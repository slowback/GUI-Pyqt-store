from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox
from module_create import *
from module_emp import *
import run_menusform
import run_empinsertform
import loginform
import sys


class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = loginform.Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEdit.setText("E001")
        self.ui.lineEdit_2.setText("9633")
        self.ui.login_button.clicked.connect(self.get_main_form)
        self.ui.login_button_2.clicked.connect(self.close)
        self.get_emp_data()

    def get_emp_data(self):
        data = select_all_employee(1)
        if len(data) == 4:
            QMessageBox.information(self, "info", "Add user data first")
            empinsert_app = run_empinsertform.MyApp(self)
            empinsert_app.ui.label_3.setVisible(False)
            empinsert_app.ui.comboBox.setVisible(False)
            empinsert_app.show()

    def get_main_form(self):
        empid = self.ui.lineEdit.text()
        emppw = self.ui.lineEdit_2.text()
        data = select_employee(empid, emppw)
        if not data:
            QMessageBox.information(self, "info", "Log in Fail")
            self.ui.lineEdit.setFocus()
        else:
            menu_app = run_menusform.MyApp(self)
            empid = menu_app.windowTitle() + " by " + empid
            menu_app.setWindowTitle(empid)
            emptype = 0
            for row in data:
                emptype = row[2]
            if emptype == 1:
                menu_app.ui.pushButton.setEnabled(True)
                menu_app.ui.pushButton_4.setEnabled(True)
                menu_app.ui.actionemployee.setEnabled(True)
            else:
                menu_app.ui.pushButton.setEnabled(False)
                menu_app.ui.pushButton_4.setEnabled(False)
                menu_app.ui.actionemployee.setEnabled(False)
            menu_app.show()


if __name__ == "__main__":
    create_table()
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
