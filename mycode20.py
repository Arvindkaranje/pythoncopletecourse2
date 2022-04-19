# 29
# exercise
# pattern printing

"""
true
*
**
***
****
"""
n=int(input("enter the number "))
m=int(input("enter one more number "))
if n==m:
    for i in range(4):
        for j in range(i+1):
            print("* ",end=" ")
        print()
    print("bye")
else:
    for i in range(4):
        for j in range(4-i):
            print("* ",end=" ")
        print()
    print("bye again")

"""
false
****
***
**
*
"""