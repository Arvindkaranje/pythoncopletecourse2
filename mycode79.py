# 102
# conclusion of the course python for absolute beginners
# create your own website and store all the technologies whichever you learn
# create blogging and store all your codes with notes there
# 103
# practice problem 1
# your age in 2022
# take age or year of birth as an input from the user and say them when will they turn 100 years
# don't use any module ,they can then optionally provide a year and your program must tell their
# age in that particular year
# you should be handling all sorts of errors like
# you are not at  born
# you seems to be the oldest person alive
# you can also handle any other errors if possible

if __name__=="__main__":
    while True:
        a=int(input("Enter your current age or your birth year here= "))
        p=int(input("Enter any random year to check your age in that particular age= "))
        if a<=125 and p>2022:
            print("Your current age is ",a)
            b=100-a
            c=b+2022
            print(f"In {c} your age will be 100years")
            m=p-2022+a
            print(f"In {p} your age will be {m}")
        elif a>=1900 and a<=2022 and p>2022:
            d=2022-a
            print("Your current age is ",d)
            e=100-d
            f=e+2022
            print(f"In {f} your age will be 100 years")
            n=p-2022+d
            print(f"In {p} your age will be {n}")
        elif a>2022:
            print("Your not yet born")
        elif a<1900:
            print("You seems like to old,i think your age is more then 123 years")
        z=input("press c to continue the process once again and q to quit the process= ")
        if z=='c':
            continue
        elif z=='q':
            exit()
        else:
            print("you have given invalid input please give valid one among these two")



