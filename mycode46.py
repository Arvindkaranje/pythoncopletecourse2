# 61
# multiple inheritance
# one class inherits multiple class with the rule of method resolution order ,,mro
#
class A:
     def a(self):
        print("class a is printing")

class B:
    def a(self):
        super(B, self).a()
        print("class b is printing")

class C(B,A):
    def a(self):
        super(C, self).a()
        print("class c is printing")

d=C()
d.a()
