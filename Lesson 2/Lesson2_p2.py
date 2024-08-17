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
            print('Số dư:', self.balance)
        else:
            print('Số tiền nạp không hợp lệ')
                
    # Phương thức rút tiền
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Tài khoản {self.account_number} đã rút {amount} VND thành công')
            print('Số dư:', self.balance)
        else:
            print('Số tiền rút không hợp lệ')

# acc1 = BankAccount('16102011',100)
# acc1.deposit(50)
# acc1.withdraw(50)

# Bài tập 2:
class Animal():
    def __init__(self, type, name, age, color, weight):
        self.type = type
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    
    def __str__(self) :
        return f'{self.type} {self.name} {self.age} {self.color} {self.weight}'
    
    def display(self):
        print(f'''
Loài: {self.type} 
Tên: {self.name} 
Tuổi: {self.age} 
Màu sắc: {self.color} 
Cân nặng: {self.weight}''')
    
a1 = Animal('human', 'Khang Anh', 12, 'rainbow', 50)
print(a1)
a1.display()