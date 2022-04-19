# 42
# time module
# check the time between while loop and for loop with time.time() function
#print time.asctime(time.localtime(time.time))
import time
first=time.time()
print(first)

for i in range(7):
    print("hiii")
    time.sleep(5)
print("after for loop ",time.time()-first)

second=time.time()
print(second)
i=0
while i<7:
    print("hello")
    i+=1
print("after while loop ",time.time()-second)
print(first-second)
import time

print(time.asctime(time.localtime(time.time())))
