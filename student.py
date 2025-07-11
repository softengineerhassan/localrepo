class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg_marks(self):
        total = 0
        for val in self.marks:
            total += val
        print("Hi" , self.name, "your average score is: " ,total/4)






s1 = student("Ali Hassan", [56,34,67,54])
s1.avg_marks()
s2 = student("Moeed",[67,45,67,34])
s2.avg_marks()
s3 = student("Farhad",[45,67,87,54])
s3.avg_marks()