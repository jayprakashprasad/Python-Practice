# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
li=[1,2,4,5]
n1=np.array(li)
print(n1)

n2=np.array([[1,2,3,4],[4,3,2,12]])
print(n2)
print(type(n2))

n3=np.full((2,2),10)
print(n3)

n4=np.arange(1,20,2)
n5=np.arange(1,20)
print(n4)
print(n5)

n6=np.random.randint(1,10,5)
print(*n6*2) #* to get rid of brackets
print(*n6)

n1.shape=(4,1)
print('\n',n1)

n2.shape=(4,2)
print('\n',n2)

nn1=np.array([10,11,12,13])
nn2=np.array([10,20,30,12])
print('\n',np.vstack((nn1,nn2)))
print('\n',np.hstack((nn1,nn2)))
print('\n',np.column_stack((nn1,nn2)))

print('\n',np.intersect1d(nn2,nn1))
print('\n',np.setdiff1d(nn1,nn2))
print('\n',np.setdiff1d(nn2,nn1))

print('\n',np.sum([nn1,nn2]))
print('\n',np.sum([nn1,nn2],axis=0))
print('\n',np.sum([nn1,nn2],axis=1))

nn2=nn2+1
print(nn2)
nn2=nn2/2
print(nn2)

rn=np.array([10,11,12,13,16,18,19])
print(np.median(rn))
print(np.mean(rn))
print(np.std(rn))


















