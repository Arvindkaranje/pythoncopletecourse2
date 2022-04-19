#create a program to guese the given number
#number of gueses 5
#print number of gueses remaining
#if guese over it should print game over
#number of gueses we used to win this game

n=18

for i in range(1,6):
    p = int(input("enter the number "))
    if n==p:
        print('your answer is correct')
        print(i,'guesses u have used to win this game')
        break
    elif i==5:
        print("game over u tried all your attempts")
    else:
        print('u have entered the wrong number please try again')
        print(5-i,"number of attempts are remaining")
        continue

