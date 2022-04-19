# 51
# decorators

def arvind(a,b):
    print(a//b)

def karanje(some):

    def kiccha(a,b):
        if b>a:
            a,b=b,a
        return some(a,b)
    return kiccha


arvind=karanje(arvind)
arvind(2,4)

