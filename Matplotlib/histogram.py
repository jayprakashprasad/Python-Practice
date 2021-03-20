
import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd
##
x=[1,2,34,4,4,4,5,6,8,6,6,6,6]
plt.hist(x)
plt.show()

##histogram  as printing dataframe


p1=pd.DataFrame({'Name':['wasssup','jay','hello','raj','anush','vivek']
    ,'Marks':[10.,20.,30.,40.,50.,60.]
    ,'loggedIn':['jay','praksh','prasad','vevek','nama','namm']
    ,'logOut':['me','you','he','she','who','i']
    ,'blogger':['me','you','he','she','who','i']
})
print(p1,'\n')
print(p1.head(),'\n')

plt.hist(p1['logOut'],color="g")
plt.show()

#another

x=[1,2,54,67,76,7,98,9,6,6,6,7,9,9,9,9,9,99,77,67]
y=[0,10,20,30,40,50,50,60,70,80,90,100]

plt.hist(x,y,histtype='bar')
plt.show()