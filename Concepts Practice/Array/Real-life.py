from array import *
import sys

current_index=-1

max_index=7*1440


def addReading(temperatureData,data):
    global current_index, max_index
    if current_index==max_index:
        front=1
        back=0
        temperatureData.pop(0)
        while(front!=max_index+1):
            temperatureData[back]=temperatureData[front]
            back+=1
            front+=1

        temperatureData[back]=data
        

    else:
        current_index+=1
        temperatureData.append(data)
        
def showData(temperatureData):
    for i in range(0,current_index+1):
        print(temperatureData[i])


def averageTemperature(temperatureData):

    temp=0
    for i in range(0,current_index+1):
        temp+=temperatureData[i]

    return temp/current_index+1

def findMinMax(temperatureData):
    min=temperatureData[0]
    max=temperatureData[0]
    for i in range(0,current_index+1):
        if(min>temperatureData[i]):
            min=temperatureData[i]
        elif(max<temperatureData[i]):
            max=temperatureData[i]

    return min,max

def flagDetect(temperatureData):
    temp=0
    for i in range (current_index-60,current_index+1):
        temp+=temperatureData[i]

    if temp/60>5 :
        return True
    else:
        return False

def compressed(temperatureData,compressedData):
    for i in range(0,current_index):
        if temperatureData[i+1]-temperatureData[i]>0.5:
            compressedData.append(temperatureData[i+1])


#1
temperatureData = array('i')



#2
for i in range(0,max_index):
    if i%2==0:
        addReading(temperatureData,(i+1)+1000)
    else:
        addReading(temperatureData,i*2)

#3
print("The average of the temperature of previous 7 days is : " ,averageTemperature(temperatureData))

#4
min,max=findMinMax(temperatureData)
print("The min temperature is : {} and the max temperature is {} ".format(min,max))


#5
print("Is past 60 min is flaged -> " , flagDetect(temperatureData))

#6
compressedData=array('i')
compressed(temperatureData,compressedData)

#7
my_list=temperatureData.tolist()

print("The memory usage by the array ",sys.getsizeof(temperatureData))
print("The memory usage by the list ", sys.getsizeof(my_list))

#8

