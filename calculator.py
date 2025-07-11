class calculator:
    def add (self, a,b):
        return a+b
    
    def subtract(self, a,b):
        return a-b
    
    def devide(self, a,b):
        if b==0:
            print("devider must be greater than 0")
        else:
            return a/b
        
calc = calculator()

print("addition of a and b is: " ,calc.add(44,33))
        





