# 104
# last or first problem solution

# 105
# second problem question

# divide the apples
""" harry potter has n number of apples,harry has some students, he wants to distribute the apples
these n number of apples are provided to harry by his friends and he can request few more or few
less apples"""

# you need to print whether a number in range min to max is a divisor or not
# input > n , min , max
# print whether numbers between min and max are divisor of n or not
# if min==max show this is not a range ,show the results

# example
# if n=20 min=2 and max=5
# 2 is divisor of 20
# 3 is not divisor of 20
# 4 is divisor of 20
# 5 is divisor of 20

n=int(input("enter the number of apples  "))
min=int(input("enter the min "))
max=int(input("enter the max "))
if min==max and n%min==0 and n%max==0:
    print(f"its not a range because both min and max are same...yes both min and max are "
          f"divisor by {n}")
elif min==max and n%min!=0 and n%max!=0:
    print(f"its not a range because both min and max are same...No both min and max are"
          f" not divisor by {n}")

if min<n and max<n and min!=max:
    for i in range(min,max+1):
        while min<=max:
            if n%min==0:
                print(f"yes {min} is divisor by {n}")
            else:
                print(f"{min} is not divisor by {n}")
            min=min+1







