# 54
# instance varibale and class variables in oops
# create a class with instance and class variables

class arvind:
# class variable is here it could be with all objects
    wheels=6
    pass

c=arvind()
d=arvind()

print(c.wheels)
arvind.wheels=8
print(c.wheels,d.wheels)
