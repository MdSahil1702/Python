from numpy import *


def checkIfSquare(matrix):
    row=0
    col=0
    for i in range(matrix.shape[0]):
        row+=1
    for j in range(matrix.shape[1]):
        col+=1

    if row==col:
        return True
    else:
        return False

def checkIfSymmetric(matrix):
    found=False
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i==j:
                break
            else:
                if matrix[i,j]==matrix[j,i]:
                    found=True
                else:
                    found=False
    return found

def antidiagonal(matrix):
    n = matrix.shape[0]
    for i in range(n):
        for j in range(matrix.shape[1]):
            if i + j == n - 1:
                print(matrix[i, j], end=" ")
                break

#1
m1=matrix('123;456;789')

#2
m2= zeros((4,4))
fill_diagonal(m2,1)
print(m1)

#3
m3=empty((5, 5))
for i in range(m3.shape[0]):
    for j in range(m3.shape[1]):
       m3[i][j]=random.randint(1,101)

#4
print(m2[2][3])


#5
m3[1][2]=99

#6
for i in range(m3.shape[1]):
    print(m3[1][i],"  ",end='')
print("")

#7
for i in range(m3.shape[0]):
    print(m3[i][2],"  ",end='')
print(" ")

#8
m4=empty((5,5))
for i in range(m4.shape[0]):
    for j in range(m4.shape[1]):
        m4[i][j]=m3[j][i]

#9
m5=m4+m3

#10
m5*=2

#11
if array_equal(m3,m4):
    print("Equal Matrix")
else :
    print("The matrix isn't equal")

#12
if m3.ndim==m5.ndim:
    m6=m3*m4
    print(m6)
else:
    print("The dimension of the matrix isn't equal" )
    
#13
print(m6.sum())

#14
print("the max element is :",m6.max(),"and the min element is :",m6.min())

#15
print("Is Matrix a square matrix ? ->",checkIfSquare(m3))

#16
m7 = matrix([
    [1, 2, 3, 4, 5, 6, 7],
    [2, 8, 9, 1, 2, 3, 4],
    [3, 9, 10, 5, 6, 7, 8],
    [4, 1, 5, 11, 9, 2, 3],
    [5, 2, 6, 9, 12, 4, 1],
    [6, 3, 7, 2, 4, 13, 5],
    [7, 4, 8, 3, 1, 5, 14]
])
print("Is matrix is symmetric? ->",checkIfSymmetric(m7))

#17
print(diagonal(m7))

#18
print(antidiagonal(m7))


#19
m8= matrix([[1,2,3],[4,5,6],[7,8,9]])
m9= matrix([[2,3,4],[5,6,7],[8,9,0]])

m10=m9+m8
print(m10)

#




























