# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#'\n',
import pandas as pd

hx=(20)#just ofr math eg
print(hx*0.5)
print(hx/0.5)


p1=pd.DataFrame({
    'Name':['wasssup','jay','hello','raj','anush','vivek']
    ,'Marks':[10,20,30,40,50,60]
    ,'loggedIn':['jay','praksh','prasad','vevek','nama','namm']
    ,'logOut':['me','you','he','she','who','i']
    ,'blogger':['me','you','he','she','who','i']
})
print(p1,'\n')
print(p1.head(),'\n')
print(p1.head(3),'\n')
print(p1.describe(),'\n')
print(p1.shape,'\n')
print(p1.tail(4),'\n',)

#pd.merge("","",on="") #for two table in same place

#print(p1.iloc[0:5,0:])
print(p1.iloc[0:5,0],'\n',)
print(p1.loc[0:5,('loggedIn','logOut')],'\n')

#print(p1.drop('blogger',axis=1,inplace=True),'\n',)
print(p1.drop('blogger',axis=1),'\n',)
print(p1.drop([3,4],axis=0),'\n') #1 drop column / 0 drop row
print(p1)

print((p1[p1.blogger != 'me']),'\n')

def double(s):
    return s*2
print(p1[['Marks','loggedIn']].apply(double))

for x in range(1):
    print(p1['Marks'])
    print((p1['loggedIn']),'\n')
  

print(p1['logOut'].value_counts())








