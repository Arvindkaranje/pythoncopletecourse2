# 67
# specail methods and operator overloading
# __Add ,__truedivision
# special methods overloading
# repr and str methods ,if str available object prints str

class employee:

    def __init__(self,sal):
        self.sal=sal

    def __add__(self, other):
        v3=self.sal+other.sal
        return v3

    def __truediv__(self, other):
        v4=self.sal//other.sal
        return v4

    def __gt__(self, other):
        if self.sal>other.sal:
            return True

arvind=employee(1010431)
priya=employee(50000)

print(arvind+priya)
print(arvind/priya)

if arvind>priya:
    print("arvind is most paid than her")
else:
    print("priya is most paid than her husband")
