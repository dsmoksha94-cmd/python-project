class parent:
    def display(self):
        print("This is the parent class")
class Child(parent):    
    def show(self):
        print("This is the child class")
obj=Child()
obj.display()
obj.show()