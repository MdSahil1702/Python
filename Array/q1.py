from array import *
import sys


#1
new_ar= array('i',[5,10,15,20,25])

#2
new_ar.insert(0,30)
#3
new_ar.insert(1,12)

#4
new_ar.remove(15) 

#5
print(new_ar.pop())


#6
print(new_ar[3])

#7
new_ar[1]=99

#8
arr1=array('i')
arr1= new_ar[1:5]
print(arr1)


#9
print(new_ar.count(20))

#10
#print(new_ar.index(25)) on available in the array

#11
print(new_ar[::-1])
#or
for i in range(len(new_ar)-1,-1,-1):
    print(new_ar[i])
    
#12
my_list=new_ar.tolist()

#13
mylist=[100,200,300]
new_ar1=array('i',mylist)

#14
new_ar.extend(arr1)

#15
new_ar1.clear()

#16
print(new_ar.itemsize)

#17

new_ar2=array('u','hello')
print(new_ar2)
#18
new_ar3=array('f',[1.5,2.5,3.5])

#19
ls=list(range(1000))
new_ar4= array ('i',range(1000))

print(sys.getsizeof(ls),"bytes of list")
print(sys.getsizeof(new_ar4),"bytes of array")

#20
new_ar5=array('i',[1,2,3,4,5,6])

try:
    new_ar5.append("hello")
except TypeError as e:
    print("Madherchod kya daal rha hai")
