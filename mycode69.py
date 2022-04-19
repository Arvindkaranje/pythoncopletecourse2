# 86
# regular expressions
import re

mystring="""arvind karanje is one of the most verstile persom of our village and he did
lot of acheivments in his life as we all know he has been working for a company with 1cr 
package and : he is also a good youtuber who contributed lot of videos to share his knowledge
that people can get some knowledge from him 
;as we all know now he is a millanior because he made lot of money now with respect to lot of 
bussiness,office work and youtube earnings ..agan we can say him as allien becuase of his mading 
his madelong aish
"""

# print(mystring)

# all the inbuilt functions from the re module to split or divide string
# findall, search, split, submodule, finditer

# patt=re,compile(r'.') all chars
# patt=re.compile(r'.ad') any char then ad
# patt=re.compile(r'^ar') string starting point
# patt=re.compile(r'g$') end with this alphabet
# patt=re.compile(r'ai*') all the a and i alphabets
# patt=re.compile(r'ai{1}') ai for how many number of time
# patt=re.compile(r'^ai{1}|t') ai for one time or t all
patt=re.compile(r'\bsh') # a word staring with these alphabets


#finditer function
matches=patt.finditer(mystring)
for i in matches:
    print(i)

print(mystring[235:245])


# print(mystring[354:357])
# print(len(mystring))

