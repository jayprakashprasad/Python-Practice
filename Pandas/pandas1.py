# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import pandas as pd
p1=pd.Series([1,2,3,4,5])
p2=pd.Series([1,2,3,4,5])
print(p1+p2)
print(p2[-3:])
print(p2[3])
print(p2[:2])


p2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(p2)

p3=pd.Series({'a':10,'b':20,'c':30},index=['c','b','a','d'])
print(p3)
print(p3[1])