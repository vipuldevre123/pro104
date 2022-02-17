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
#lets sort the data
newdata.sort()
#lets calculate median
if L%2==0:
    median1=float(newdata[L//2])
    median2=float(newdata[L//2-1])
    median=median1+median2
else:
    median=newdata[L//2]
    
print("median="+str(median))    
