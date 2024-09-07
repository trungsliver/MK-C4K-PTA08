class Animal():
    # Phương thức khởi tạo đối tượng
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    # Phương thức hiển thị thông tin
    def __str__(self):
        return f'{self.name} - {self.age} - {self.type}'
    

    def display_info(self):
        print(f"""
Name: {self.name}
Age: {self.age}
Type: {self.type}""")   
        
    # Phương thức sửa thông tin
    def change_name(self, new_name):
        self.name = new_name

    def change_name(self, new_age):
        self.age = new_age

    def change_name(self, new_type):
        self.type = new_type