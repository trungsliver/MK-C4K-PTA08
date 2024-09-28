import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import login, signup

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()
users = ['admin:admin']

def homeUi():
    global ui
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_signup.clicked.connect(signup_check)
    MainWindow.show()

def login_w():
    global ui
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.btn_signup.clicked.connect(signup_check)
    MainWindow.show()

def signup_check():
    check = True
    name = ui.lineEdit_name.text().strip()
    username = ui.lineEdit_email.text().strip()
    password = ui.lineEdit_password.text().strip()
    confirm = ui.lineEdit_confirm.text().strip()
    # Thiếu thông tin
    if name == '' or username == '' or password == '' or confirm == '':
        check = False
        msg_box('Signup fail', 'Missing information!')
    # Pass và confirm không khớp
    elif password != confirm:
        check = False
        msg_box('Signup fail', 'Password and confirm password are not match!')
    # Đã tồn tại username trong danh sách users
    else:
        for user in users:
            stored_username, stored_password = user.split(':', 1)
            if username == stored_username:
                check = False
                msg_box('Signup fail', 'Username already exists!')
    
    # Kiểm tra xem có đang ký thành công không
    if check == True:
        # Add tài khoản mới vào danh sách users
        new_acc = username + ':' + password
        users.append(new_acc)
        msg_box('Signup success', 'Signup success!')
        print(users)
        login_w()



def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

#Run app
homeUi()
sys.exit(app.exec())

# Lưu ý: chuột phải vào folder chứa 2 file này, chọn Open .... terminal
# Câu lệnh convert ui: pyuic6 -x login.ui -o login.py
# Câu lệnh convert ui: pyuic6 -x signup.ui -o signup.py
# Câu lệnh convert qrc: pyside6-rcc img.qrc -o img_rc.py