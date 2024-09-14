import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import lesson5

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = lesson5.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

#Run app
homeUi()
sys.exit(app.exec())

# Câu lệnh convert: pyuic6 -x lesson5.ui -o lesson5.py