from functools import *
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result) # 150

result=reduce(lambda x,y:x*y,l)
print(result)   #12000000

from functools import *
result=reduce(lambda x,y:x+y,range(1,101))
print(result)   #5050