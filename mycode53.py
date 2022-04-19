# 69
# we can't create any objects to object base class
# getters and setters
# set attributes in class
# and get attributes using objects

class employee:

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname


    def fullname(self):
        print(f"ths is {self.fname} {self.lname}")

    @property
    def email(self):
        print(f"{self.fname}{self.lname}@gmail.com")

    @email.setter
    def email(self, string):
        print("Setting now")
        names=string.split ("@") [0]
        self.fname=string.split(",") [0]
        self.lname=string.split(",") [1]


agk=employee("arvind","karanje")
# print(agk.fname,agk.lname)
# agk.fname='priya'
# agk.lname='swamyandkaranje'
# agk.email
agk.email='kiccha,sudeep'
agk.email
agk.fullname()
print(agk.fname)
print(agk.lname)