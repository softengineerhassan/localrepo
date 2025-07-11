class employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def information(self):
        print(f"dear {self.name} your position is {self.position} and your salary is {self.salary}")



e1 = employee("Hassan", "python developer", 100000)
e1.information()
e2 = employee("Ali", "backend Developer", 200000)
e2.information()