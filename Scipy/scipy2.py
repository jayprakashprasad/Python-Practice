import scipy as sp
from scipy import fftpack
from scipy import linalg
import numpy as np


var1=np.array([[1,2,3,4],[2,3,4,5]])
fun1=sp.fft(var1)
print(fun1)

##
var1=np.array([[1,2],[2,3]])
var2=np.array([[3,4],[9,5]])
print(sp.linalg.solve(var1,var2))

function1=sp.linalg.inv(var1)
print(function1)
