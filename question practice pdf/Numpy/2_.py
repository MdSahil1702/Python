import numpy as np 

#array creation and properties
#1
a= np.arange(10)
print(a)
a=a.tolist()
print(a)

#2
a= np .arange(12).reshape(3,4)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.ndim)

import matplotlib.pyplot as plt

#3

import sys
a= np.arange(1000)
b=list(range(1000))

print("size of 1000 element array numpy", a.nbytes)
print("size of 1000 element list", sys.getsizeof(b))


#4
a=np.arange(12).reshape(3,4)
a=a.reshape(2,6)
print(a)

#5
a= np.identity(5,int)
print(a.diagonal())





#advance 
#1
x= np.linspace(0,10,20)
y=x**2

# plt.plot(x,y)


import math as mth

#2
x=np.linspace(0,2*mth.pi,100)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Sine and Cosine Curves")
plt.legend()
plt.grid(True)
# plt.show()