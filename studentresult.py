class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avgCal(self):
        total = 0
        for val in self.marks:
            total += val
        average = total / len(self.marks)
        print("Hi", self.name, "your average score is:", average)


s1 = Student("Hassan", [45, 67, 45, 67, 45])
s1.avgCal()

s2 = Student("Ali", [34, 67, 54, 87, 54])
s2.avgCal()
