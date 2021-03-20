import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import scipy as sp
import numpy as np

data=sb.load_dataset('dots')
print(data)

sb.distplot(data['time'])
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import scipy as sp
import numpy as np

data=sb.load_dataset('tips')
print(data)

#sb.distplot(data['time'])
#sb.jointplot(x='tip',y='total_bill',data=data)
#sb.catplot(x='month',y='passengers',data=data,kind='violin')
#kind='strip,box'
graph=sb.FacetGrid(data,col='total_bill',hue='tip')
graph.map(plt.scatter,'sex','smoker')
plt.show()
