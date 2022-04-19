#13
#create set
#list inside the set
#add some values to set
#duplicate values not allow in the set
#union
#intersection
#len,max,min,type,
#difference
#symetric difference
#remove

a={1,2,3,4,4,4,2,3,1}
print(a)
a.add(10)
print(a)

b={99,44,44,22,2,1,3}
print(a|b)
print(a&b)
print(a-b)
print(a^b)

print(len(a),min(a),max(a))

a.remove(4)