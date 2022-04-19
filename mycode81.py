# 106
# problem 2 solution

# 107
# problem 3 question
# foods and calories

# you visit restaurant called arvind and food items in this restaurant are sorted based on their
# amount of calories,you have tio reverse this list of food items their calories

# you have to use following methods to reverse a list
# inbuilt method of python
# listname[::-1] slicing trick
# swapping first element with last one and second item with second last so on

# input
# take list as an input from user
# [2,3,4,6]

# output
# [6,4,3,2]
# [6,4,3,2]
# [6,4,3,2]
# all the three methods should give the same output

# creating list with user input
arvind=[]
n=int(input("Enter the length of the list "))
for i in range(n):
    x=int(input("enter the values here"))
    arvind.append(x)

print("actual list is here")
print(arvind)
reverse2=arvind[:]
reverse3=reverse2[:]
print(id(arvind),id(reverse2),id(reverse3))

while True:
    print("press 1 to reverse the list using inbuilt method")
    print("press 2 to reverse the list using index slicing method")
    print("press 3 to reverse the list using swapping method")
    print("press 4 to quit the process")
    z=int(input())

    if z==1:
        print("converted with first method using inbuilt method")
        arvind.reverse()
        print(arvind)

    elif z==2:
        print("converted with second method using index slicing technique")
        print(reverse2[::-1])

    elif z==3:
        print("converted with third method using swapping")
        p=reverse3[0]
        q=reverse3[-1]
        for i in range(len(reverse3)//2):
            p, q = q, p
            p=reverse3[-1]-1
            q=reverse3[0]+1
        print(reverse3)

    elif z==4:
        exit()
    else:
        print("wrong input please try again")


