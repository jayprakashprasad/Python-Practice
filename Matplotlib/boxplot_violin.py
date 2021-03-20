

from matplotlib import pyplot as plt

##

##box plot
x=[1,2,3,4,5,6,7,8,9]
y=[1,2,3,4,5,4,3,2,1]
z=[6,7,8,9,6,5,7,8]

data=list([x,y,z])
#plt.boxplot(data)
plt.violinplot(data,showmedians=True)
print(plt.show())