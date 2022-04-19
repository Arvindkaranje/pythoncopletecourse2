# 34
# recursion
# function inside the function
# get factorial of the number using recursion
# quiz write a fibonacci
import sys

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

def fib(n):
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=" ")

n=int(input("enter any number "))
fib(n)




