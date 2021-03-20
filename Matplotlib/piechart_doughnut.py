
from matplotlib import pyplot as plt

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
