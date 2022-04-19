# 33
# global variable and global keyword
# local variable and global variable
# nested functions to try global variables

# this is global variable and it can be changed inside the function as well with the global
# keyword ,,using global keyword inside the function we can update the value of global var
a=10

def arvind():
    global a
    #initially this was local variable but here we used global keyword and changed this
    #local variale into global variable
    a=18
    print("inside functon ",a)

arvind()
print("outside the function ",a)


