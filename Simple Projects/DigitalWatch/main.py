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
