# 48
# map, filter and reduce function
# create a list with string values and convert those values as int values ,using map function
# create one more list with int values and print the square root number of those numbers using
# map and lambda

# create a list of some numbers and use filter function to print those numbers which are less
# than 5,also print those numbers with some addition value for each of the values of the list

# from functools import reduce
# create a list and use reduce function to reduce the length of the list

from functools import *
a=['3','4','6','3','9']

s=list(map(int,a))
print(s)

b=[1,2,3,4,5,6,7,8]

c=list(map(lambda n:n*n,b))
print(c)

d=[1,2,3,4,5,6,7,8,9]
e=list(filter(lambda n:n>5,d))
print(e)

p=(reduce(lambda a,b:a+b,d))
print(p)
