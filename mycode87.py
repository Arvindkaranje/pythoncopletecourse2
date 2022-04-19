# 118
# problem 8 solution

# 119
# problem 9 question
# funny names

"""Its result day of school and not everyone is so happy there . you decide to  make your friends laugh by jumbling their
names to come up with some funny names"""
"""your program should take the number of names and the names separated by space as input. output should be funny 
names in the same order"""

# input
# enter total number of friends
# 3
# enter the names of your 3 friends
# rohan das
# shubham agarwal
# ritesh arora

# output
# rohan agarwal
# ritesh das
# shubham arora

# hint
# split function to split the first name and second name of the friends
# random module to swap the names

import random
n=int(input("Enter the total number of friends= "))

s=[]
for i in range(n):
    m=input("enter the names here ")
    s.append(m)

j=str(s)
k=j.split()

