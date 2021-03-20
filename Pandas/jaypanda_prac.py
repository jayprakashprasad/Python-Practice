
import pandas as pd
  
p2=pd.DataFrame({'Name':['wasssup','jay','hello','raj','anush','vivek']
    ,'Marks':[10,20,30,40,50,60]
    ,'loggedIn':['jay','praksh','prasad','vevek','nama','namm']
    ,'logOut':['me','you','he','she','who','i']
    ,'blogger':['me','you','he','she','who','i']
     ,'mm':[60,50,40,30,201,203]
})
for x in range(1):
    print(p2['Marks'])
    print((p2['loggedIn']),'\n')

print(p2,'\n')  
p3=p2.sort_values(by='mm')
p4=p2.sort_values(by='Marks')
p5=p3+p4
print(p5)

