#1
import numpy as np
import pandas as pd

do_readings= pd.read_csv("C:\Coding Section\IIITV\Python\question practice pdf\Pandas\BKB_WaterQualityData_2020084.csv")

do_readings=do_readings['Dissolved Oxygen (mg/L)']
print(do_readings)