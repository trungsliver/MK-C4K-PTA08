class Human():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f'Tôi tên là {self.name}, {self.age} tuổi')

class Student(Human):
    def __init__(self, name, age, gender, school):
        super().__init__(name, age, gender)
        self.school = school

    def introduce(self):
        print(f'Tôi tên là {self.name} học tại {self.school}')

class Animal():
    def __init__(self, ten, loai):
        self.ten = ten
        self.loai = loai
    def eat(self):
        print(f'{self.ten} đang ăn')
    def sleep(self):
        print('khò khò')

class Dog(Animal):
    def __init__(self, ten, loai, giong):
        super().__init__(ten, loai)
        self.giong = giong
    def eat(self):
        print('nhoàm nhoàm')
    def bark(self):
        print('gâu gâu')