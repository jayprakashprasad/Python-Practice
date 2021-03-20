import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

person={'finanace':[3,4,5,6,7,7,8,8,3,3,5,5,5],
      'management':[1,2,3,4,4,5,6,6,6,7,8,3,8],
       'logistics':[2,5,5,7,7,8,9,9,0,0,5,4,3],
        'get_work':[2,5,3,4,4,5,6,2,2,6,0,5,4]
}
data=pd.DataFrame(person,columns=['finanace','management','logistics','get_work'])
print(data)

x=data[['finanace','management','logistics']]
y=data['get_work']

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=0)

lr=LogisticRegression()
lr.fit(X_train,Y_train)
Y_prediction=lr.predict(X_test)

conf_mat=pd.crosstab(Y_test,Y_prediction,rownames=['True'],colnames=['Prevision'])
sn.heatmap(conf_mat,annot=True)

print('Accuracy:',metrics.accuracy_score(Y_test,Y_prediction))
plt.show()
