import csv
import pandas as pd
from collections import Counter


with open('dataset.csv',newline='') as f:
    file=csv.reader(f)
    file_data=list(file)

#print(file)

print(file_data)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    num=file_data[i][1]
    #print(num)

    new_data.append(float(num))


#mean
num_of_data=len(new_data)

total = 0

for z in new_data:
    total+=z

mean=total/num_of_data

print('Mean: ',mean)

#median
new_data.sort()

print(num_of_data)

if num_of_data % 2 == 0:
    median1=float(new_data[num_of_data//2])
    median2=float(new_data[(num_of_data//2)+1])

    median=(median1+median2)/2

else:

    median=float(new_data[num_of_data//2])

print('Median: ',median)

data=Counter(new_data)

mode_data= {
    '50-60':0,
    '60-70':0,
    '70-80':0
}

for height,occurence in data.items():
    if 50 < float(height) < 60:
        mode_data['50-60']+=occurence
    elif 60 < float(height) < 70:
        mode_data['60-70']+=occurence
    elif 70 < float(height) < 80:
        mode_data['70-80']+=occurence
    

mode_range,mode_occurence = 0,0

for q,occurence in mode_data.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(q.split('-')[0]),int(q.split('-')[1])],occurence

print('mode range',mode_range)
mode=float((mode_range[0]+mode_range[1])/2)


print('Mode: ',mode)





