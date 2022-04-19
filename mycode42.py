# 55
# self ,__init__,or constructor in oops
# create a class and define a method inside to use self
# init method is used to get the arguments from the object with self and constructor
class arvind:

    # constructor and init method to create instance method and instance variables
    def __init__(self,name,sal,prof):
        self.name=name
        self.sal=sal
        self.prof=prof
        # self will consider as the object name everytime
    def details(self):
        print(f"the name is {self.name} the salary is {self.sal} and the proffession is {self.prof}")

c=arvind('arvind','10lpa','software developer')
# c.name='arvind'
# c.sal='5lpa'
# c.prof='software engineer'

c.details()