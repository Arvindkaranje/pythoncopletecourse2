# 117
# problem 8 question
# rohan das is a fraud

"""rohan das was wrote a python function to  print a multiplication table of a given number and put one of the value
(randomly generate)as wrong"""
# rohan das did this to fool his classmates and make them commit a mistake in the test .you cannot tolerate this
# so you decided to use your python skills to counter rohan's actions by writing python program to validates rohan's
# multiplication table
# your function should be able to find out the wrong values in rohan's table and expose rohan das as a fraud

# note: rohan's function returns list of numbers like this

# input
# rohanmultiplication(2)

# output
# [2,4,6,8,10,12,14,11,16,18,20]

# you have to write the function iscorrect(func,number) and return the index where rohan's function is wrong and point
# it to the screen if the table is correct your function returns none

import random
# taking random place into table to generate the wrong value
k=random.randint(2,9)
print(k)
s=[]
def rohanmultipliation(n):
    """ this function defines the multiplication of number in list,firstly starting the loop with 1 and stopping at 10
    and one of the value would be wrong according to requirement and takin that value with random module again"""
    for i in range(1,11):
        if i==k:
           r=random.randint(1,30)
           s.append(r)
        else:
             m=n*i
             s.append(m)
    return s

# taking a number from the use to generate the multiplication table
n=int(input("Enter any number which you want to get as multiplication table= "))
print(rohanmultipliation(n))


def iscorrect(s):
    """This function is made to test the above function rohanmultiplication(n) whether its returning the correct
    multiplication table or not . if its printing any of the value as incorrect this function will ping the error or
     wrong value and shows the index of that value which is incorrect , else its returns none"""
    for i in range(1,11):
        if s[i-1] != i*n:
            return i-1
    return None

print(iscorrect(s))
