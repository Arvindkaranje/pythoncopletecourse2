# 108
# solution problem 3

# 109
# problem 4 question

# the next palindrome

# problem content
# a palindrome is a string which when reversed is equal to itself
# example of palindrome 616,mom,10001,101
""" you have to take a number as an input from the user.you have to find the next palindrome of
corresponding to that number.your first input should be 'number of taste cases' and then take
 all the cases as input from the user"""

# input
# number of test cases 3
# first case 4
# second case 105
# third case 534

# output
# next palindrome for 4 is 10
# next palindrome for 105 is 111
# next palindrome for 534 is 535
def is_palindrome(numbers):
    return str(numbers)==str(numbers)[::-1]

def next_palindrome(numbers):
    numbers=numbers+1
    while not is_palindrome(numbers):
        numbers += 1
    return numbers

cases=int(input("Enter the number how many times u want to perform this next palindrome of num "))
numbers=[]
for i in range(cases):
    num=int(input("enter the values here "))
    numbers.append(num)
print(numbers)

gum=[]
for i in range(cases):
    if i<10:
        gum.append(numbers[i])
    if i>=10:
        gum.append(next_palindrome(numbers[i]))

    # print(f"next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
print(gum)




