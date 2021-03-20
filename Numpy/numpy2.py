# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np

#multi dimensional array

nn1=np.array([[10,11,12,13],[10,11,12,13]])
nn2=np.array([[10,20,30,12],[10,11,12,13]])
print('\n',np.vstack((nn1,nn2)))
print('\n',np.hstack((nn1,nn2)))
print('\n',np.column_stack((nn1,nn2)))

print('\n',np.intersect1d(nn2,nn1))

print('\n',np.setdiff1d(nn1,nn2))
print('\n',np.setdiff1d(nn2,nn1))

print('\n',np.sum([nn1,nn2]))
print('\n',np.sum([nn1,nn2],axis=0))
print('\n',np.sum([nn1,nn2],axis=1))