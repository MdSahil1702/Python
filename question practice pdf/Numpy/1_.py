#BASIC: Array Creation & Properties
import numpy as np
#1

matrix1d=np.array([10, 20, 30, 40,
50])

print(matrix1d)

#2
zeroesmatrix= np.zeros((3,4))
print(zeroesmatrix)

#3
identitymatrix= np.eye(3)
print(identitymatrix)

#4
fourmatrix= np.linspace(0,1,10)
print(fourmatrix)

#5
fivematrix= np . random . randint (5 , 16 , (2 , 3) ) 
print(fivematrix)

#6
sixmatrix = np.full((2,2,2),7)
print(sixmatrix)

#7
sevenmatrix = np.array([[1,2,3],[4,5,6]])

print(sevenmatrix.shape)
print(sevenmatrix.ndim)
print(sevenmatrix.size)
print(sevenmatrix.dtype)


# -----------------------------------


#Indexing, Slicing & Reshaping

#1
onematrix=np.array([10,20,30,40,50,60])
print(onematrix[2:5])

#2
twomatrix=np.arange(1,13).reshape(3,4)
print(twomatrix[1:3,0:3])

#3
threematrix= np.array([1,5,8,2,9,3])
result= threematrix[threematrix>5]
print(result)

#4
fourmatrix=np.arange(1,13).reshape(4,3)
print(fourmatrix)
fourmatrix=fourmatrix.flatten()
print(fourmatrix)

#5
fivematrix=np.array([1,2,3,4,5]).reshape(-1,1)
print(fivematrix)
print(fivematrix.reshape(1,-1))

#6
sixmatrix=np.arange(0,12).reshape(2,3,2)
print(sixmatrix)


#-------------------------------

#Vectorized Operations
