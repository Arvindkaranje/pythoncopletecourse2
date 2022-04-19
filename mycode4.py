#create list
l=[1,2,3,4,5,'arvind']
#index slicing
print(l[:])
#assign some more numbers in existing list
l[5]=8
print(l)

#reverse list,sort list,
l.reverse()
print(l[:])

#index skip 2
print(l[0:6:2])


#len,max,min,append,,insert,remove,pop
print(len(l),max(l),min(l))

#update some value
l.append(('karaje'))
print(l)

l.remove(8)
print(l)

l.insert(2,77)
print(l)

l.pop()
print(l)

#create tuple
tup=(1,2,3,4,5,65,77)
print(tup)
#try to updete

#do index slicing
print(tup[:-1])
#use some inbuilt methods
print(len(tup))





