# 64
# polymorphism
# many forms or various forms
# 65
# method overriding and super keyword
# variable overriding and super keyword

class priya:
    course='bcom'
    def __init__(self):
        self.name='priya'
        self.sal=30000

    def love(self):
        print("she is priya")

class arvind(priya):
    course = 'mca'
    def __init__(self):
        super(arvind, self).__init__()
        self.name='arvind karanje'
        self.sal=100000


    def love(self):
        super(arvind, self).love()
        print("he is arvind")

a=arvind()
print(a.name,a.sal)

a.love()