# 30
# more on file
# tell function ,seek function

# opened the funciton with the variable f and will be in defualt mode which will be read mode
f=open('priya.txt')

# reading all the lines using read function with the variable f
print(f.read())

#using tell function with f variable which will simply show the present index of the file
print(f.tell())

#using seek function which will go back to the file and print all the stafs whicheve
#is pending
print(f.seek(190))

# closing the file with the close function and f variable
f.close()