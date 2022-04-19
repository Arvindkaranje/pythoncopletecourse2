# 56
# class methods in python

class arvind:
    eng=89
    kann=99

    def __init__(self,p,c,m,b):
        self.p=p
        self.c=c
        self.m=m
        self.b=b

    def pcmb(self):
        m3=self.p+self.c+self.m+self.b
        print(m3)

    @classmethod
    def langsub(cls):
        m4=cls.eng+cls.kann
        print(m4)


student1=arvind(88,87,66,77)
student2=arvind(88,56,77,65)


