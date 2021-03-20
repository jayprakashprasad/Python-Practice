
import numpy as np 
from matplotlib import pyplot as plt

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