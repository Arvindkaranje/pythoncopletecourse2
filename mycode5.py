#10
#create dictionary
#add element with assignment
#delet item from dict
#update function
#print all keys
#print all values items
#copy()
dailytasks={'morning':'code herry','aftnoon':'naveen redyy','evening':'sql udemy','night':'enlishpract'}
dailytasks['latnight']='somemotivat'
print(dailytasks)
dailytasks.__delitem__('night')
print(dailytasks)
print(dailytasks.keys())
print(dailytasks.items())
print(dailytasks.values())

#create a dictionary and take input from the user and return the meaning of the word from the dictionary

mydict={'impact':'=effect','aspirants':'candidates','list':'mutable','tuple':'imutable'}

inmp=input(("enter the word which u want to know "))
print(inmp,mydict[inmp])

