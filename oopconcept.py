class student():
    def __init__(self,fullName, rollNumber):
        self.name = fullName
        self.rollnumber = rollNumber

    def welcome(self):
         print("welcome students!",self.name)

    def getMarks(self):
        return self.rollnumber
           
       
        


s1 = student("Hassan", 78)
print(s1.name)
#print(s1.rollnumber)
s1.welcome()
print(s1.getMarks())


s2 = student("Moeed", 89)
print(s2.name)
print(s2.rollnumber)
s2.welcome()