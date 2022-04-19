# 28
# more with file handling
# writing a file and appending something to existing file

f=open("priya.txt",'r+')
print(f.read())
print(f.write("i just wanna say i love u forever"))
print((f.read()))
f.close()