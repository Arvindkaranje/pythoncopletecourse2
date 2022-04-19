#24
#exception handling
#try
#except exception
#finaly

a=5
b=0

try:
    print(a/b)
except ZeroDivisionError:
    a,b=b,a
    print(a/b)
finally:
    print("done with it ")