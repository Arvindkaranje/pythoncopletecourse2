# 112
# solution of problem 5

# 113
# problem 6 question
# guess the number

"""Generate a random integer from a and b . you and your friend have to guess the number between two numbers a and b
 a and b are the inputs taken from the user. your friend is player1 and plays first. he will have to keep choosing the
 number and your program must tell whether the number is  greater than the actual number or less than the actual number
  .log the number of trials it look your friend to arrive at the number , you play the same game and then the person
  with minimum number of trials wins!"""

# randomly generate a number and do not show that to user (say6)

# input
# enter the value of a
# 4
# enter the value of b
# 13

# output
# player 1:
# please guess the number between 4 and 13
# 5
# wrong guess ,guess greater value than this
# 7
# wrong guess again, guess smaller value than this

import random

a=int(input("Enter the value for a= "))
b=int(input("Enter the value for b= "))
c=random.randint(a,b)

m=b-a
i=1
for i in range(1,m+1):
    print("Player 1 is playing now ")
    d=int(input(f"Please guess the number between {a} and {b} = "))
    if d==c:
        print(f"Well done you have guessed the correct number in attempt")
        break
    elif d>c:
        print(f"wrong guess but try again with smaller value than {d}")
    elif d<c:
        print(f"wrong guess but try again with bigger value than {d} ")
    elif d<a:
        print(f"you have entered the wrong input please guess between {a} and {b}")

j=1
for j in range(j,m+1):
    print("Player 2 is playing now")
    f=int(input(f"Enter the number between {a} and {b}= "))
    if f==c:
        print(f"well done you have guessed the correct number in attempt")
        break
    elif f>c:
        print(f"wrong guess but try again with smaller value than {f}")
    elif f<c:
        print(f"wrong guess but try again with bigger value than {f}")
    elif f<a:
        print(f"you have entered the wrong input please guess between {a} and {b}")

print(f"Player 1 took {i} number of attempt to guess the actual number ")
print(f"Player 2 took {j} number of attempt to guess the actual number ")

if i>j:
    print("player 2 won the game")
elif i==j:
    print(f"Both are took same {i} and {j} attempts so match is tied ")
else:
    print("Player 1 won the game")




