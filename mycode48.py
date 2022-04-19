# 63
# public, private and protected access specifiers
# _protected
# __private

# public >>it can be accessed by everyone
# protected >> this can be accessed by only few peoples who have authorization to access
# private variables are not accessed by anyone ,only the creators or the main class can access it
# with managling


class arvind:
    _aruu=219
    def _priya(self):
        print("hi aruuu")

    __kiccha = 8833

    def __asha(self):
        print("hello karanje")

class karanje(arvind):
    pass

d=karanje()
print(d._aruu)
print(d._arvind__kiccha)
d._priya()
d._arvind__asha()

