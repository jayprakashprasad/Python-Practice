import numpy as np
import matplotlib.pyplot as plt

x=np.array([12,3,4,5,6,7,87,8,9,6,5.3,54])
y=np.array([2,3,4,4,5,5,6,7,7,4,3,7,7,6,67,7,7,4])
func1=np.polyfit(x,y,1)

plt.plot(x,y,'.')
plt.plot(x,np.polyval(func1,x),'r-')
plt.show()