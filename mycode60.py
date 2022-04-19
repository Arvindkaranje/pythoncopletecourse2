# 76
# else and finally with try and except keywords
# finally is used to file clean up or something operation which should be performed apart from
# the try and except
# else will be executed if the except block doesn't work
# we can write multiple exceptions

try:
    print("hello")
except Exception as e:
    print(e)
else:
    print("this also went wrong")
finally:
    print("close the file if opened")



