# 79
# os module
# os module is used to handle the operations with files and folders

import os
# it shows the all features which will be provided os module
# print(dir(os))

#current working directory
#print(os.getcwd())

#changining working directory
#os.chdir("c://")

#opening some files from working directory
#open(file name)

#all the files from working directory
# print(os.listdir())
# print(os.listdir("C://"))

# creating folder using mkdir()
# os.mkdir("this")

# rename the any file
# os.rename('arvind.txt','asha.txt')

# print(os.environ.get("path"))

# joining two paths
# print(os.path.join("c:/", "harry.txt"))

# checking the existing paths with the values true and false
print(os.path.exists("C://program"))



