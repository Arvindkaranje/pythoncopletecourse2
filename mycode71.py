# 88
# exercise 8 solution time
# 89
# raise exception and stop iteration or further execution
# use if else and check condition and raise exception
# use some loop to raise exception and stop iteration
# raise zero division error
# raise value error
# raise some more errors

# a=input("what is your name ")
# b=input("what is your salary ")

# if int(b)==0:
# raise Exception("your salary is 0 so sorry we cant do the further process of this program")

# if a.isnumeric():
# raise Exception("sorry numeric numbers are not allowed here")

s=list()
n=int(input("enter the length of list"))

def nums(n):
    for i in range(n):
        x=int(input("enter the int values here "))
        s.append(x)
    for i in s:
        if i>=9:
            raise Exception("we can iterate the bigger numbers then ",i)
nums(n)

# task >> use two exceptions from python
# search built in exceptions




