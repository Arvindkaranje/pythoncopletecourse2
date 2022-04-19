# 57
# class method as alternative constructors
# create a class method
class student:
    eng=88

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def total(self):
        print("total is",self.m1+self.m2)

    @classmethod
    def languages(cls, newm):
        cls.eng=newm

    @classmethod
    def from_str(cls,string):
        params=string.split("-")
        return cls(params[0])



s1=student(88,99)
s1.total()
s1.from_str(99)