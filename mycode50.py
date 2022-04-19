# 66
# diamond shape problem
# method resolution order
# multiple inheritance with 4 classes
# a single class can inherit multiple clsses and we can get all the feautetrs from all the classes
# c++ and python supports multiple inheritance

class A:
    def pri(self):
        print("class a is printing ")

class B(A):
    def pri(self):
        super(B, self).pri()
        print("class b is printing ")

class C:
    def pri(self):
        super(C, self).pri()
        print("class c is printing ")

class D(C,B):
    def pri(self):
        super(D, self).pri()
        print("class d is printing ")
    
a=A()
b=B()
c=C()
d=D()

d.pri()

