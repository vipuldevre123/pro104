from collections import Counter
import csv
from itertools import count
with open('heightweight.csv',newline='') as f:
    r=csv.reader(f)
    data=list(r)

    
#lets remove the column name from data
data.pop(0)

#lets store the data of height
newdata=[]
totaldata=len(data)

for i in  range(totaldata):
    n=data[i][1]
    newdata.append(float(n))

#lets calculate mode
d=Counter(newdata)  
mode_data_for_range = { 
    "50-60": 0,
    "60-70": 0,
    "70-80": 0 } 
for height, occurence in d.items():
     if 50 < float(height) < 60: 
         mode_data_for_range["50-60"] += occurence 
     elif 60 < float(height) < 70: 
         mode_data_for_range["60-70"] += occurence 
     elif 70 < float(height) < 80:
         mode_data_for_range["70-80"] += occurence 
mode_range, mode_occurence = 0, 0 
for range, occurence in mode_data_for_range.items(): 
    if occurence > mode_occurence: 
         mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence 
mode = float((mode_range[0] + mode_range[1]) / 2) 
print(f"Mode is -> {mode:2f}")  