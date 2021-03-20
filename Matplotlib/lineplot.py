import numpy as np 
from matplotlib import pyplot as plt
x=np.arange(1,11)
print(x)
y1=2*x
y2=3*x
print(y1)
print(y2)
plt.plot(x,y1,color="g",linewidth="2",linestyle=":")
plt.plot(x,y2,color="r",linewidth="4",linestyle=":")
plt.grid(True)

plt.ylabel("numbers")
plt.xlabel("x-axis")
plt.title("plot")
print(plt.show())
###


import numpy as np 
from matplotlib import pyplot as plt
x=np.arange(1,11)
print(x)
y1=2*x
y2=3*x
print(y1)
print(y2)
plt.subplot(2,1,1)
plt.plot(x,y1,color='r',linestyle=":",linewidth="4")


plt.subplot(2,1,2)
plt.plot(x,y2,color='y',linestyle=":",linewidth="4")
plt.grid(True)

plt.ylabel("numbers")
plt.xlabel("x-axis")
plt.title("plot")
print(plt.show())
