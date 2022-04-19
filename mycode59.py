# 75
# function caching in python
import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    print("i love u priya")
    time.sleep(n)
    print("love u2 arvind")

if __name__=="__main__":
    print("first call")
    some_work(2)
    print("second time calling")
    some_work(2)
    some_work(2)


# create a function and ask user for cache
