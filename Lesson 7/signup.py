# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal ExtraBold")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 300, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 350, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 400, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(200, 150, 500, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(200, 300, 500, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(200, 350, 500, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_confirm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_confirm.setGeometry(QtCore.QRect(200, 400, 500, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(12)
        self.lineEdit_confirm.setFont(font)
        self.lineEdit_confirm.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_confirm.setObjectName("lineEdit_confirm")
        self.dateEdit_dob = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit_dob.setGeometry(QtCore.QRect(200, 200, 150, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.dateEdit_dob.setFont(font)
        self.dateEdit_dob.setObjectName("dateEdit_dob")
        self.checkBox_male = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_male.setGeometry(QtCore.QRect(200, 255, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.checkBox_male.setFont(font)
        self.checkBox_male.setObjectName("checkBox_male")
        self.checkBox_female = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_female.setGeometry(QtCore.QRect(300, 255, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.checkBox_female.setFont(font)
        self.checkBox_female.setObjectName("checkBox_female")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(420, 255, 80, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(520, 255, 80, 35))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(650, 260, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btn_signup = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(310, 480, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal ExtraBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btn_signup.setFont(font)
        self.btn_signup.setStyleSheet("border-radius: 20px;\n"
"border: 1px solid black;\n"
"background: rgb(166, 254, 255)")
        self.btn_signup.setObjectName("btn_signup")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SIGN UP"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_3.setText(_translate("MainWindow", "DOB:"))
        self.label_4.setText(_translate("MainWindow", "Gender:"))
        self.label_5.setText(_translate("MainWindow", "Email:"))
        self.label_6.setText(_translate("MainWindow", "Password:"))
        self.label_7.setText(_translate("MainWindow", "Confirm:"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "Input your name"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "Email adress"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_confirm.setPlaceholderText(_translate("MainWindow", "Confirm password"))
        self.checkBox_male.setText(_translate("MainWindow", "Male"))
        self.checkBox_female.setText(_translate("MainWindow", "Female"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Others"))
        self.btn_signup.setText(_translate("MainWindow", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
