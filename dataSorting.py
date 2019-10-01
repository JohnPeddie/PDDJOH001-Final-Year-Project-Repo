#! python3
from statistics import mean


def getUsefulData(lines,maxLat,minLat,maxLong,minLong):
    
    usefulLines = []
    for line in lines:        
        dataArray = line.split()
        if (len(dataArray) >2):
            if ((float(dataArray[2]) <= maxLat) and (float(dataArray[2]) >= minLat) and (float(dataArray[3]) <= maxLong) and (float(dataArray[3]) >= minLong) ):
                usefulData = [dataArray[2],dataArray[3],dataArray[5],dataArray[6],dataArray[0]] #LAT, LONG, Salinity, Temp, Date
                usefulLines.append(usefulData)
    
    return(usefulLines)

def compileGridPositions(maxLat,minLat,maxLong,minLong):
       
    lat = maxLat-minLat
    long = maxLong-minLong
    latLongGrid= [[[] for x in range(long+1)] for y in range(lat+1)] 
    return latLongGrid
    
    
def averageSalinityPerBlock(limitedData, maxLat, minLat, maxLong, minLong):
    salinityGrid =compileGridPositions(maxLat, minLat, maxLong, minLong)
    #print (salinityGrid)
    for item in limitedData:
        lat = int(float(item[0]))
        long = int(float(item[1]))
        salinity = float(item[3])
        #print("lat: ",lat, " long: ",long)
        gridLat = abs(lat - maxLat)
        
        gridLong = long - minLong
        #print (gridLat)
        #print(gridLong)
        salinityGrid[gridLat][gridLong].append(salinity)
    xgrid =[]
    ygrid = []
    
    for x in salinityGrid:
        for y in x:
            if (len(y)>0): 
                ygrid.append(mean(y))
            else:
                ygrid.append([])
        xgrid.append(ygrid)
        ygrid= []
                
    return xgrid

def heatMap(data):
    print("latitudes")
    for lat in data:
        print (lat[0])
    print("Longatudes")
    for long in data:
        print (long[1])
    print("data")
    for salt in data:
        print (salt[2])       
def gridToExcel(salinityGrid,maxLat, minLat, maxLong, minLong):
  
    print("Latitudes")
    lats = []
    for lat in range(minLat,maxLat+1):
        for i in range((maxLong-minLong)+1):
            lats.append(lat)
            
              
           
    lats.reverse()
    
    for l in lats:
        print(l)
    
    
    print("Longatudes")
    for j in range((maxLat-minLat)+1):
        for long in range(minLong,maxLong+1):
            print (long)
    print("Data average:")
    for x in salinityGrid:
        for y in x:
            if (y!= []):
                print(y)
            else: 
                print(0)
        


with open ('WINTER_2016.txt', 'r') as file:
    maxLat = -30
    minLat = -36
    maxLong= 31
    minLong=17     
    file_contents = file.read()
    lines = file_contents.split('\n')
    limitedData = getUsefulData(lines,maxLat,minLat,maxLong,minLong)
    salinityGrid = averageSalinityPerBlock(limitedData,maxLat, minLat, maxLong, minLong)
    gridToExcel(salinityGrid,maxLat, minLat, maxLong, minLong)
    #heatMap(limitedData)
    
    
    