# Lập trình hướng đối tượng - OOP
class Human:
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender, price):   
        # name, age, gender, price là thuộc tính
        self.name = name
        self.age = age
        self.gender = gender
        self.price = price
    
    # Phương thức __str__ để dùng được print
    def __str__(self):
        return f'{self.name} {self.age} tuổi {self.gender}: {self.price} VND'

    def greeting(self):
        print(f'{self.name} xin chào tất cả mọi người!')

    def change_name(self):
        self.name = 'not found'

# human1 = Human('Khang Anh', 12, 'meow', 1)
# human2 = Human('Duc Tung', 13, 'gay', 10)
# human3 = Human('Minh Tu', 13, 'beo', 0)
# human4 = Human('Bao Phuc', 15, 'male', 32.5)
# human5 = Human('Chi Bao', 11, 'male', 80)
# human6 = Human('Tuan Minh', 12, 'mail', 0)
# print(human1)
# human1.change_name()
# print(human1)

class Rectangle:
    def __init__(self, a, b):
    # Thuộc tính: a - chiều dài, b - chiều rộng
       self.a = a
       self.b = b
    # Phương thức tính chu vi
    def cvi(self):
        return (self.a + self.b)*2
    # Phương thức tính diện tích
    def dtich(self):
        return self.a * self.b

# hcn1 = Rectangle(5, 2)
# hcn2 = Rectangle(10, 3)
# print('Chu vi HCN1:', hcn1.cvi())
# print('Diện tích HCN1:', hcn1.dtich())
# print('Chu vi HCN2:', hcn2.cvi())
# print('Diện tích HCN2:', hcn2.dtich())
    
# Bài tập 1: class BankAccount với các thuộc tính account_number và balance. 
    # Sử dụng các phương thức deposit() - nạp và withdraw() - rút để cập nhật số dư.
class BankAccount():
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        
    # Phương thức nạp tiền
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Tài khoản {self.account_number} đã nạp {amount} VND thành công')
        else:
            print('Số tiền nạp không hợp lệ')
                
    # Phương thức rút tiền
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Tài khoản {self.account_number} đã rút {amount} VND thành công')
        else:
            print('Số tiền rút không hợp lệ')

acc1 = BankAccount('16102011')
acc1.deposit(50)
acc1.withdraw(50)
print('hello')