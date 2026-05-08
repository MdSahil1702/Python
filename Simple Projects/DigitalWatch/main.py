import time
import os
from  datetime import datetime
#functions are declare and define here
def showTimer():
    while 1:
        os.system('cls') 
        curr_time= datetime.now()
        print(   f"{curr_time.hour:02d} : "
            f"{curr_time.minute:02d} : "
            f"{curr_time.second:02d}")
        time.sleep(1)
    return 

def setTime():
    hr=int(input("Enter the hour(0-24)"))
    if hr>24 or hr<0:
        print("Wrong input")
        return
    
    min=int(input("Enter the minute"))
    if min>60 or min<0:
        print("Wrong input")
        return
    
    sec=0
    while True:

        os.system('cls')  
       

        print(f"{hr:02d}:{min:02d}:{sec:02d}")
        time.sleep(1)
        sec += 1

        if sec == 60:
            sec = 0
            min += 1

        if min == 60:
            min = 0
            hr += 1

        if hr == 24:
            hr = 0
    

def Timer():
    print("Enter the timestamp")
    hr=int(input("Enter the hour(0-24)"))
    if hr>24 or hr<0:
        print("Wrong input")
        return
    
    min=int(input("Enter the minute"))
    if min>60 or min<0:
        print("Wrong input")
        return
    sec =60
    while True:
        
        os.system('cls')  
       

        print(f"{hr:02d}:{min:02d}:{sec:02d}")
        
        if hr == 0 and min == 0 and sec == 0:
            print("\nTime Up!")
            break
        time.sleep(1)
        sec -= 1

       

        if sec < 0:
            sec = 59
            min -= 1

        if min < 0:
            min = 59
            hr -= 1
             
      
                
        
            
    

while 1:
    print("1. Show Time\n"
        "2.Set Time\n"
        "3.Timer\n"
        "4.Exit\n")

    userinput=int(input("Choose your option"))

    if userinput==1:
        showTimer()
    elif userinput==2:
        setTime()
    elif userinput==3:
        Timer()
    elif userinput==4:
        print("Exiting the program")
        break
