class Overloading:
    
    def add(self, a=None, b=None, c=None):
        
        if a is not None and b is not None and c is not None:
            return a + b + c
        
        elif a is not None and b is not None:
            return a + b
        
        elif a is not None:
            return a
        
        else:
            return 0
obj = Overloading()

print("Addition of 2 numbers:", obj.add(10, 20))
print("Addition of 3 numbers:", obj.add(10, 20, 30))
print("Addition of 1 number:", obj.add(10))
