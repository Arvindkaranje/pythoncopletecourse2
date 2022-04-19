# 31
# how to open file "with block"

# opened the file using with block and it will be closed by defaultly
# here we are using a variable called f to get access to the file and reading all the text
# from th file priya.txt
with open('priya.txt') as f:
    print(f.read())