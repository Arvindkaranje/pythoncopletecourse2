# 68
# abstract base class
# abstract method
# abc module abstractmethod
# the classes whichever inherits base class ,should have the abstractmethod with it

from abc import ABC , abstractmethod

class shape(ABC):
    @abstractmethod
    def totallength(self):
        return 0

class rectangle(shape):

    def __init__(self):
        self.left=4
        self.right=5

    def totallength(self):
        print(self.left+self.right)

c=rectangle()
c.totallength()





