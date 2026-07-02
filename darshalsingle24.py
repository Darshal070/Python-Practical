# Single Inheritance
class A:
    def show(self):
        print("This is Parent class")


class B(A):
    def display(self):
        print("This is Child class")
obj = B()

obj.show()      
obj.display()    
