import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import login, signup

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_signup.clicked.connect(signup_check)
    MainWindow.show()

def signup_check():
    print('signup')

#Run app
homeUi()
sys.exit(app.exec())

# Lưu ý: chuột phải vào folder chứa 2 file này, chọn Open .... terminal
# Câu lệnh convert ui: pyuic6 -x login.ui -o login.py
# Câu lệnh convert ui: pyuic6 -x signup.ui -o signup.py
# Câu lệnh convert qrc: pyside6-rcc img.qrc -o img_rc.py