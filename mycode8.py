#faulty calculator


#design the calculater which will correctly solve all the problems except the following and your program should take
#operator and the two numbers as input from the user
#45*3=555, 56+9=77, 56/4=4

a=eval(input("enter the operation here "))

if a==45*3:
    print(555)
elif a==56+9:
    print(77)
elif a==56/4:
    print(4)
else:
    print(a)