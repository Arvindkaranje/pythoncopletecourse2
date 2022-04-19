# 110
# problem 4 solution

# 111
# problem 5 question
# palindromify the list

"""you are given a list which contains some numbers ,you have to print a list of next palindromes only if the number
is greater than 10 . other wise you have to print the number itself"""

# input
# [1,2,4,5,78,8,79

# output
# [1,2,4,5,88,8,88]

def is_palindrome(s):
    return str(s)==str(s)[::-1]

def next_palindrome(s):
    s=s+1
    while not is_palindrome(s):
        s += 1
    return s

n=int(input("enter the length of the list "))
s=[]

for i in range(n):
    m=int(input("enter the values here "))
    if m<10:
        s.append(m)
    else:
        s.append(next_palindrome(m))

print(s)

# print(s)
# m=[]
# for i in s:
#     if i<10:
#         m.append(i)
#     else:
#         m.append(next_palindrome(i))
#
# print(m)





