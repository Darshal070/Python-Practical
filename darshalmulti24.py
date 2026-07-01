# Multilevel Inheritance

class Grandparent:
    def show_grandparent(self):
        print("This is Grandparent class")


class Parent(Grandparent):
    def show_parent(self):
        print("This is Parent class")


class Child(Parent):
    def show_child(self):
        print("This is Child class")


# Create object
obj = Child()

obj.show_grandparent()
obj.show_parent()
obj.show_child()
