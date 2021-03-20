
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

X,Y_true=make_blobs(n_samples=800,centers=5,cluster_std=0.45,random_state=0)

plt.scatter(X[:,0],X[:,1], s=30)

func=KMeans(n_clusters=4)
func.fit(X)
Y_func=func.predict(X)

plt.scatter(X[:,0],X[:,1],c=Y_func,s=15)
centers=func.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='red' , s=75, alpha=1)
plt.show()