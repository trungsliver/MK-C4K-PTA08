# Data Types
    # String - chuỗi ký tự
name = 'Khang Anh'
    # Int - số nguyên
age = 25
    # Float - số thực
score = 6.5
    # Bool/Boolean - True/False
die = True

# Các kiểu print
    # Cách 1: Dùng dấu +
# print('Họ tên: ' + name + 'Tuổi: ' + str(age))
    # Cách 2: Dùng dấu ,
# print(name, age, score, die, 'hihi')
    # Cách 3: Dùng f - truyền dữ liệu vào string
# print(f'{name} được {score} trong bài kiểm tra')

# Input - Nhập dữ liệu
    # Xác định kiểu dữ liệu: type()
# print(type(name), type(age), type(score), type(die))
    # Ép kiểu khi input
# a = int(input('Nhập số nguyên bất kỳ: '))

# Các phép toán:
    # Thông thường: + - * /
    # Chia lấy nguyên: //
    # Chia lấy dư: %
    # Lũy thừa: **

# Câu điều kiện:
    #  Các phép so sánh: == != <= >= < >
    #  Các phép toán: and - or - not
    #  Cấu trúc/Dạng:
        # Dạng thiếu: if
        # Dạng đủ: if else
        # Dạng đa nhánh: if elif elif ... else

# Vòng lặp hữu hạn - Vòng lặp for
    # range(n): chạy từ 0 đến n-1
    # range(start, stop, step):

# Vòng lặp vô hạn - Vòng lặp while
    # while <điều kiện>: lặp đến khi điều kiện sai

# Danh sách: CRUD
    # C - Create: PTA08 = []
    # R - Read: Duyệt, in danh sách
        # Cách 1: for i in range(len(arr)):
        # Cách 2: for item in arr:
        # Cách 3: for index, item in enumerate(arr):
        # Cách 4: print(arr)
    # U - Update:
        # append(item): thêm phần tử vào cuối danh sách
        # insert(index, item): thêm phần tử vào vị trí chỉ định
        # arr[i] = new_value
    # D - Delete:
        # remove(item): xóa bằng giái trị
        # pop(index): xóa bằng chỉ số index
        # clear(): xóa tất cả phần tử
    # Sắp xếp:
        # sort(): nhỏ => lớn
        # sort(reversed= True): lớn => nhỏ
    # Khác:
        # len(): trả về độ dài (số phần tử danh sách)
        # min(): trả về item nhỏ nhất
        # max(): trả về item lớn nhất

# Các thao tác với chuỗi ký tự:
    # len(): độ dài chuỗi
    # split(): tách chuỗi
    # replace(old_str, new_str): thay thế
    # strip(): xóa khoảng trắng ở đầu và cuối
    # 1 số hàm viết hoa, viết thường
# name = 'dUc tRunG sIeU cAp vIPprO'
        # Viết hoa tất cả
# name2 = name.upper()
        # Viết thường tất cả
# name2 = name.lower()
        # Viết hoa chữ cái đầu của mỗi từ
# import string
# name2 = string.capwords(name)
# print(name2)

# Hàm/Chương trình con
    # Hàm có giá trị trả về (return)
    # Hàm có tham số truyền vào: chuvi(cdai, crong)
# def cviHCN(a, b):
#     return (a+b)*2
# print(cviHCN(age,5))