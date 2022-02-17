import csv
#lets open the file
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

    
L=len(newdata)
#lets add all the new data numbers
total=0
for i in newdata:
    total=total+i

mean=total/L    
print("mean="+str(mean))