#pass
#break
#continue

#write a program which will take inputs from user and print the numbers continuesly till 100
#whenever the given number of user reached greater than 100 u should simply print cangrats


while (True):
    n=int(input("enter the number "))
    if n>=100:
        print("cangrats")
        break
    else:
        print("try again")
        continue
