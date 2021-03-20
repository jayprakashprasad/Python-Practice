import numpy as np 
from matplotlib import pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[10,12,13,14,15,16,18,20]
z=[4,5,9,4,8,4,9,41]

plt.scatter(x,y,marker="*",c="black",s=60)
plt.scatter(x,z,marker=".",c="r",s=60)

plt.subplot(1,2,1)
plt.scatter(x,y,marker="*",c="black",s=60)

plt.subplot(1,2,2)
plt.scatter(x,z,marker=".",c="r",s=60)

print(plt.show())