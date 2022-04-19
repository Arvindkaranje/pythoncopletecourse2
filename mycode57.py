# 73
# python list comprehensions
# print a even numbers upto 50 using normal code
# comprehence that code into one code
# all data structors comprehesions
# dictionary comphrehensions
# reverse key values with comprehension

#normal code which will be converted as comprehesion list
from sympy import *

lst=[]
for i in range(50):
    if i%2==0:
        lst.append(i)
print(lst)

#list comprehension
j=[i for i in range(50)  if i%2==0]
print(j)
print(type(j))

# dictionary comprehension
k={i:f"item{i}" for i in range(20) if i%2==0}
print(k)

# list comprehension
m={dress for dress in ['dress1 ,dress2']}
print(m)

# generator comprehension
odds=(i for i in range(1,21) if i%2==0)
for i in odds:
    print(i)

for i in range(1,50):
    if i % 1 == 1:
        print("its a prime number")
    else:
        print("its not a prime")
print(isprime(5))

    # question
# take a list from users


