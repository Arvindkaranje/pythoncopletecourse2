# 70
# object introspection
# type
# id
# dir
# import inspect module and print getmembers

class employee:

    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    def details(self):
        print(f"this is {self.name} and he has {self.sal} salary")

c=employee('arvind',100000)
d=employee('priya',50000)

print(id(employee),id(c),id(d))
print(type(employee),type(c),type(d))
print(dir(employee))
print(dir(c))
