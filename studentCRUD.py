import json
import os

STUDENT_FILE = "studentrecord.json"

class Student:
    def __init__(self,name,rollNumber,clas,marks):
        self.name = name
        self.rollnumber = rollNumber
        self.clas = clas
        self.marks = marks

    def to_dict(self):
        return{
            "name": self.name,
            "rollNumber": self.rollnumber,
            "clas": self.clas,
            "marks": self.marks
        }
class Managestudent:
    def __init__(self):
        self.Student = []
        self.load_data()

    def load_data(self):
        if os.path.exists(STUDENT_FILE):
            with open (STUDENT_FILE,'r') as file:
                data = json.load(file)
                for item in data:
                    self.Student.append(Student(item["name"],item["rollNumber"],item["clas"],item["marks"]))
    def save_data(self):
        with open(STUDENT_FILE, 'w') as file:
            json.dump([c.to_dict() for c in self.Student],file,indent=4)

    def add_Student(self):
        name = input("enter student name!")
        rollNumber = input("enter student's roll number!")
        clas = input("enter class")
        marks = input("marks")
        self.Student.append(Student(name,rollNumber,clas,marks))
        self.save_data()
        print("data save successfully!")

    def view_student(self):
        name = input("enter student name you want to view")
        for c in self.Student:
            if c.name.lower()==name.lower():
                print(f"name{c.name},rollNumber{c.rollNumber},clas{c.clas},marks{c.marks}")
                return
        print("not found")

    def update_student(self):
        name = input("name of student that you want to update")
        for c in self.Student:
            if c.name.lower()==name.lower():
                #c.rollNumber=input("enter new roll number")
                c.clas=input("enter new class")
                c.marks=input("enter new marks of student")
                self.save_data()
                print("updated successfully!")
                return
        print("you enter wrong name this student is not found")

    def delete_student(self):
        rollNumber = input("enter roll number that student you want to delete!")
        for c in self.Student:
            if c.rollNumber == rollNumber:
                self.Student.remove(c)
                self.save_data()
                print("deleted successfully!")
                return
        print("student not found")



manager = Managestudent()
while True:
    print("1. for add studnet")
    print("2. for view student")
    print("3. for update student")
    print("4. for delete student")

    choice = input("enter the number")

    if choice == "1":
        manager.add_Student()
    elif choice =="2":
        manager.view_student()
    elif choice == "3":
        manager.update_student()
    elif choice == "4":
        manager.delete_student()
    else: print("try again")

