import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import l4

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = l4.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

#Run app
homeUi()
sys.exit(app.exec())