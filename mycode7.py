#13>Dicsion making statements
#if else statements

#if
#else
#elif
a='aeiou'
if 'a' in a:
    print('its a vowel')
else:
    print("its a constant")



#take a number from user input which will be the age of person for the car drive licence ,give the response to the user
#according to their age if they are below u cant drive,and above 18 u can, and if equal to 18 means will tak the desc
#very soon

n=int(input("enter your age "))

if n == 18:
    print("will decide very soon")
elif n>18 and n<100:
    print("yes ur allowed to car drive")
elif n>100:
    print("your age is higher than limit")
else:
    print("your age is less than limit")
