# 62
# multi level inheritance
# each class will inherits the upper class of it
# create 3 classes
# electronic device ,pocket gadget, phone

class dad:
    def so(self):
        print("dad is here")

class son(dad):
    def so(self):
        super(son, self).so()
        print("son is here")

class grandson(son):
    def so(self):
        super(grandson, self).so()
        print("grandson is here ")

c=grandson()
c.so()


class electronicdevice:

    def etc(self):
        print('electronic machines are here ')

class pocketgadget(electronicdevice):

    def etc(self):
        super(pocketgadget, self).etc()
        print("pocket gadgets are here ")

class phone(pocketgadget):

    def etc(self):
        super(phone, self).etc()
        print("phone is here")
        
d=phone()
d.etc()