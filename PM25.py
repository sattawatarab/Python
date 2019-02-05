print("Running : requests")
import requests

url = "http://air4thai.pcd.go.th/services/getNewAQI_JSON.php"

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "keys"
    }

response = requests.request("GET", url, headers=headers)
print("Running : response.json")
data = response.json()
print("Running : dict")
dict_1=data
print("Running : pandas")
import pandas as pd
df1 = pd.DataFrame()
list_branch_stationID=[]
for item in dict_1['stations'] :
            list_branch_stationID.append(item['stationID'])
df1['stationID']=list_branch_stationID
list_branch_nameEN=[]
for item in dict_1['stations'] :
            list_branch_nameEN.append(item['nameEN'])
df1['nameEN']=list_branch_nameEN
list_branch_nameTH=[]
for item in dict_1['stations'] :
            list_branch_nameTH.append(item['nameTH'])
df1['nameTH']=list_branch_nameTH
list_branch_areaTH=[]
for item in dict_1['stations'] :
            list_branch_areaTH.append(item['areaTH'])
df1['areaTH']=list_branch_areaTH
list_branch_areaEN=[]
for item in dict_1['stations'] :
            list_branch_areaEN.append(item['areaEN'])
df1['areaEN']=list_branch_areaEN
list_branch_stationType=[]
for item in dict_1['stations'] :
            list_branch_stationType.append(item['stationType'])
df1['stationType']=list_branch_stationType
list_date=[]
for item in dict_1['stations'] :
           list_date.append(item['LastUpdate']['date'])
df1['date'] = list_date
list_time=[]
for item in dict_1['stations'] :
           list_time.append(item['LastUpdate']['time'])
df1['time'] = list_time
list_PM25=[]
for item in dict_1['stations'] :
           list_PM25.append(item['LastUpdate']['PM25']['value'])
df1['PM25'] = list_PM25
list_unitPM25=[]
for item in dict_1['stations'] :
           list_unitPM25.append(item['LastUpdate']['PM25']['unit'])
df1['unitPM25'] = list_unitPM25
list_PM10=[]
for item in dict_1['stations'] :
           list_PM10.append(item['LastUpdate']['PM10']['value'])
df1['PM10'] = list_PM10
list_unitPM10=[]
for item in dict_1['stations'] :
           list_unitPM10.append(item['LastUpdate']['PM10']['unit'])
df1['unitPM10'] = list_unitPM10
list_O3=[]
for item in dict_1['stations'] :
           list_O3.append(item['LastUpdate']['O3']['value'])
df1['O3'] = list_O3
list_unitO3=[]
for item in dict_1['stations'] :
           list_unitO3.append(item['LastUpdate']['O3']['unit'])
df1['unitO3'] = list_unitO3
df1['unitO3'] = list_unitO3
list_CO=[]
for item in dict_1['stations'] :
           list_CO.append(item['LastUpdate']['CO']['value'])
df1['CO'] = list_CO
list_unitCO=[]
for item in dict_1['stations'] :
           list_unitCO.append(item['LastUpdate']['CO']['unit'])
df1['unitCO'] = list_unitCO
list_NO2=[]
for item in dict_1['stations'] :
           list_NO2.append(item['LastUpdate']['NO2']['value'])
df1['NO2'] = list_NO2
list_unitNO2=[]
for item in dict_1['stations'] :
           list_unitNO2.append(item['LastUpdate']['NO2']['unit'])
df1['unitNO2'] = list_unitNO2
list_SO2=[]
for item in dict_1['stations'] :
           list_SO2.append(item['LastUpdate']['SO2']['value'])
df1['SO2'] = list_SO2
list_unitSO2=[]
for item in dict_1['stations'] :
           list_unitSO2.append(item['LastUpdate']['SO2']['unit'])
df1['unitSO2'] = list_unitSO2
list_AQILevel=[]
for item in dict_1['stations'] :
           list_AQILevel.append(item['LastUpdate']['AQI']['Level'])
df1['AQILevel'] = list_AQILevel
list_AQIaqi=[]
for item in dict_1['stations'] :
           list_AQIaqi.append(item['LastUpdate']['AQI']['aqi'])
df1['AQIaqi'] = list_AQIaqi
list_lat=[]
for item in dict_1['stations'] :
            list_lat.append(item['lat'])
df1['lat'] = list_lat
list_long=[]
for item in dict_1['stations'] :
           list_long.append(item['long'])
df1['long'] = list_long
print("Running : to_csv")
df1.to_csv('C:/Users/sattawat.a/Desktop/Python/PM25/PM25/PM25/outputPM25.csv')