# 72
# iterator
# generator
j=[9,8,7,6,5]
n=iter(j)
print(next(n))
print(next(n))

def aru():
    n=1
    while n<=10:
       sq=n*n
       yield sq
       n=n+1

arvind=aru()
for i in arvind:
    print(i)