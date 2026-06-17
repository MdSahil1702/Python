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
plt.show()