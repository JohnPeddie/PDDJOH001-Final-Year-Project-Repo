import csv
from collections import Counter
from statistics import mean

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

def frange(start, stop=None, step=None):
    if stop == None:
        stop = start + 0.0
        start = 0.0

    if step == None:
        step = 1.0

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield ("%g" % start) # return float number
        start = start + step

def frequincyPlotValuesForExcel(dataList):
    roundedList = []
    for i in dataList:
        roundedList.append(round(float(i),1))
    print("mean: ", mean(roundedList))    
    counted = Counter(roundedList)
    print("Rounded values:")
    for k in sorted(counted):
        print(k)
    print("Frequency:")
    for l in sorted(counted):
        print(counted[l])
        
def averageSpeed(data):
    floatList = []
    for i in data:
        floatList.append(float(i))
    return mean(floatList)
        
        
def frequincyPlotValuesForExcelAll(dataArray):
    counts =[]
    print("Frequency:")
    for d in frange(0,26,0.1):
        print(d)
        counts.append(float(d))
    for dataList in dataArray:
    
        roundedList = []
        for i in dataList:
            roundedList.append(round(float(i),1))
        
        counted = Counter(roundedList)
        
        print("Rounded values:")
        for k in counts:
            if k in counted:
                print(counted[k])
            else:
                print(0)
       
    
def roundedTest(dataList, title):
    roundedList = []
    for i in dataList:
        roundedList.append(round(float(i),1))  
    print(title+" data")
    for q in roundedList:
        print(q)

naming = ['01','02','03','04','05','06','07','08','09','10','11','12']
ws62 = []
ws60 = []
ws40 = []
ws20 = []
ws10 = []
for i in naming:  
    with open ('wm08_2018'+i+'_v01.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
       
        for line in csv_reader:
            if ((len(line)>10) and (line[0]!="date_time")): #ignore legend and headings
                ws62.append(line[2])
                ws60.append(line[6])
                ws40.append(line[10])
                ws20.append(line[14])
                ws10.append(line[18])
                


ws62 = remove_values_from_list(ws62, ' NULL')
ws60 = remove_values_from_list(ws60, ' NULL')
ws40 = remove_values_from_list(ws40, ' NULL')
ws20 = remove_values_from_list(ws20, ' NULL')
ws10 = remove_values_from_list(ws10, ' NULL')


print("Average value: ", averageSpeed(ws62+ws60+ws40+ws20+ws10))
print("Total data points: ", (len(ws62)+len(ws60)+len(ws40)+len(ws20)+len(ws10)))

frequincyPlotValuesForExcelAll([ws62,ws60,ws40,ws20,ws10])
