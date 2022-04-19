# 101
# mini project 1
# solution oops
# library management system
# creating a class as library

class Library:
    def __init__(self,list, name):
        self.booklist=list
        self.name=name
        self.lenddict={}

    def displaybooks(self):
        print(f"We have these following books in our {self.name} library")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender book database has been updated this particular"
                   " book is your responsible, you can take the book now")
        else:
            print(f"This book is already given to {self.lenddict[book]}")

    def detabaseofgivenbooks(self):
         print(self.lenddict)

    def addbook(self,book):
        self.booklist.append(book)
        print(f"{book} book has been added to library you can lend it now")

    def returnbook(self,ret,book):
        try:
            self.lenddict.pop(book)
        except Exception as e:
            print("sorry you have not took this book from us ,so we cant take it back")

if __name__=="__main__":
    agk=Library(["Python","Data science","Bhagawath geeta","Machine learning","Bio of kiccha sudeepa"
            ,"Virat kohli"],"Arvind karanje")
    while (True):
        print(f"Hello sir, Welcome to the {agk.name} library")
        print("1.press one to display the available books")
        print("2.press two to lend any books from our library")
        print("3.press three to add any new book to our library")
        print("4.press four two return the book if you have taken any book from our library ")
        print("5.press five to see the database of library")
        user_choice=int(input())

        if user_choice==1:
            agk.displaybooks()

        elif user_choice==2:
            book=input("Enter the name of the book which u want lend from our library: ")
            user=input("Enter your name for proof: ")
            agk.lendbook(user, book)

        elif user_choice==3:
            boook=input("Enter the book name which you want to add in our library :")
            agk.addbook(boook)

        elif user_choice==4:
            ret=input("Enter the book name which you want to return ")
            nam=input("Enter your name ")
            agk.returnbook(ret,nam)

        elif user_choice==5:
            agk.detabaseofgivenbooks()

        else:
            print("you have entered invalid input")

        print("press c to continue with our library or press q quit and exit")
        user_choice2=" "
        while (user_choice2!='c' and user_choice2!='q'):
            user_choice2=input()
            if user_choice2=='q':
                exit()
            elif user_choice=='c':
                continue
