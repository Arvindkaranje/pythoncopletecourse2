# 37
# exercise 5 solution
# 38
# random function
# random variable randint
# random.random *100
# random.choice with list
# assignment : take two modules and use 2,2 functions of both modules
# imported 2 modules numpy and math and worked with two modules of them

import random
from math import *
from numpy import  *

randi=random.randint(6,14)
print(randi)

rando=random.random()*100
print(rando)

lst=list()
n=int(input("enter the length of list "))
for i in range(n):
    x=input("enter the values here ")
    lst.append(x)
kst =random.choice(lst)
print(kst)

print(sqrt(5))
print(cos(1))

arr=array([1,2,3,4,5])
print(arr)
print(type(arr))






