# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
n=np.array([(12,4,5),(61,2,43)])
print(n[1:,2])
print(n[1:2])
print(n[1:2].reshape(3,1),'\n')
print(n[1:2])

jj=np.linspace(10,5,10)
print(jj.round())
print(jj)

n1=np.array([(12,4,5),(1,3,5)])
print(n.ravel())
print(n.sum(axis=1))
print(n.sum(axis=0))

print(n1[1:,].std())
print(np.std(n1))
print(np.exp(n1))

n2=np.array([1])
print(np.exp(n2))

n2=np.array([949])
print(np.log(n2))








