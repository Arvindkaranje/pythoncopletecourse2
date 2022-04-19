# 60
# inheritance
# single level inheritance
# inheritance is all about two or more classes where child class inherits the parent class get all
# the features or features of the methods from the parent class
# code reusablity

class arvind:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def address(self):
        print("his addresas is unknown")

class karanje(arvind):
    pass

a=karanje('arvind',23)
print(a.name,a.age)
a.address()

