from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(30):
            print ("Hello")
            
            
class Hi(Thread):
    def run(self):
        for i in range(30):
            print ("Hi")
            
            
obj1= Hello()
obj2 = Hi()

obj1.start()

obj2.start()