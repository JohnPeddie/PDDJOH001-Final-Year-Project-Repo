import csv
from collections import Counter
from statistics import mean

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

def hourlyMean(windSpeeds):
    hours = int(len(windSpeeds)/6)
    hourlyMeans = []
    print("Total hours: ",hours)
    for i in range(hours):
        thisHour = []
        thisHour.append(round(float(windSpeeds[0]),2))
        thisHour.append(round(float(windSpeeds[1]),2))
        thisHour.append(round(float(windSpeeds[2]),2))
        thisHour.append(round(float(windSpeeds[3]),2))
        thisHour.append(round(float(windSpeeds[4]),2))
        thisHour.append(round(float(windSpeeds[5]),2))
        del windSpeeds[0:6]
        hourlyMeans.append(mean(thisHour))
    
    return hourlyMeans

def dailyMean(windSpeeds):
    days = int(len(windSpeeds)/24)
    dailyMeans = []
    print("Total days: ",days)
    for i in range(days):
        thisDay = []
        thisDay.append(round(float(windSpeeds[0]),2))
        thisDay.append(round(float(windSpeeds[1]),2))
        thisDay.append(round(float(windSpeeds[2]),2))
        thisDay.append(round(float(windSpeeds[3]),2))
        thisDay.append(round(float(windSpeeds[4]),2))
        thisDay.append(round(float(windSpeeds[5]),2))
        thisDay.append(round(float(windSpeeds[6]),2))
        thisDay.append(round(float(windSpeeds[7]),2))
        thisDay.append(round(float(windSpeeds[8]),2))
        thisDay.append(round(float(windSpeeds[9]),2))
        thisDay.append(round(float(windSpeeds[10]),2))
        thisDay.append(round(float(windSpeeds[11]),2))
        thisDay.append(round(float(windSpeeds[12]),2))
        thisDay.append(round(float(windSpeeds[13]),2))
        thisDay.append(round(float(windSpeeds[14]),2))
        thisDay.append(round(float(windSpeeds[15]),2))
        thisDay.append(round(float(windSpeeds[16]),2))
        thisDay.append(round(float(windSpeeds[17]),2))
        thisDay.append(round(float(windSpeeds[18]),2))
        thisDay.append(round(float(windSpeeds[19]),2))
        thisDay.append(round(float(windSpeeds[20]),2))
        thisDay.append(round(float(windSpeeds[21]),2))
        thisDay.append(round(float(windSpeeds[22]),2))
        thisDay.append(round(float(windSpeeds[23]),2))
        del windSpeeds[0:24]
        dailyMeans.append(mean(thisDay))
    
    return dailyMeans
   
   
   
   
   
   
naming = ['01','02','03','04','05','06','07','08','09','10','11','12']
ws62 = []
ws60 = []
ws40 = []
ws20 = []
ws10 = []
for i in naming:  
    with open ('wm05_2018'+i+'_v01.csv', 'r') as csv_file:
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

ws62f = open("daily_WS62.txt","w+")
for ws62i in dailyMean(hourlyMean(ws10)):
    stringToWrite = str(ws62i)+"\n"
    ws62f.write(stringToWrite)

ws62f.close()
