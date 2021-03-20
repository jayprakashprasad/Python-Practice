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

##bar plot

student={'Bob':'87','julia':'86','anne':'85','matt':'95'}
name=list(student.keys())
print(name)

values=list(student.values())
print(values)
plt.bar(name,values)
plt.title("It is bar plot")
plt.xlabel("names of students")
plt.ylabel("its student marks")
print(plt.show())


##scatter plot
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

##
x=[1,2,34,4,4,4,5,6,8,6,6,6,6]
plt.hist(x)
print(plt.show())

##histogram  as printing dataframe
import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd

p1=pd.DataFrame({'Name':['wasssup','jay','hello','raj','anush','vivek']
    ,'Marks':[10.,20.,30.,40.,50.,60.]
    ,'loggedIn':['jay','praksh','prasad','vevek','nama','namm']
    ,'logOut':['me','you','he','she','who','i']
    ,'blogger':['me','you','he','she','who','i']
})
print(p1,'\n')
print(p1.head(),'\n')
plt.hist(p1['logOut'],color="g")

print(plt.show())


##box plot
x=[1,2,3,4,5,6,7,8,9]
y=[1,2,3,4,5,4,3,2,1]
z=[6,7,8,9,6,5,7,8]

data=list([x,y,z])
#plt.boxplot(data)
plt.violinplot(data,showmedians=True)
print(plt.show())

###pie chart

fruit=['apple','mango','pinapll','grapes']
quantity=[8,9,3,3]
plt.pie(quantity,labels=fruit,autopct='%0.1f%%',colors=['yellow','blue','blue','black'])
print(plt.show())

####same as
fruit=['apple','mango','pinapll','grapes']
quantity=[8,9,3,3]
plt.pie(quantity,labels=fruit,radius=1.2,autopct='%0.1f%%')
plt.pie([200],radius=0.6,colors=['w'])

print(plt.show())

