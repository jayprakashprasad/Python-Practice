# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#22/9/20
import datetime
x = datetime.datetime.now().strftime("%y")
xi = datetime.datetime.now().month
print(x)
print(xi)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))


li=[1,2,2]
lis=[]
for x in li:
    lis.append(x**2)
print(lis)
lis2=(list(map(lambda x: x**2,li)))
print(lis2)



sz=1+2
def Display(zi,zii):
    z=zii+zi
    print(z)
    

def main():
   
    Display(10,2)
    return 2
    
main()

##
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    for i in range(1, 10 + 1):
     print (N, "x", i, "=", N*i)





































