# 77
# coroutines in python
# coroutines are something that can process a time consuming  function at a time and that will
# produce all the operation withing second whenever we call that function second time but the
# first process time will be taken as usual

def searcher():
    import time
    # doing some operation which will take four seconds of time
    print("first process started wait for 3 seconds")
    book="this is a book on  harry and code with harry and good"
    time.sleep(3)
    print("first process is over,wait for 2 seconds")
    time.sleep(2)

    while True:
        text=(yield )
        if text in book:
            print("your text is in the book")
        else:
            print("your text is not in the book")

search=searcher()
next(search)
search.send("and")
print("next method run")
search.send("harry")
search.send("my name is arvind karanje")
search.send("something is there")
search.send("code with harry")

