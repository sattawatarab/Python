# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Sattawat Arab
# GIS Analyst
# i-bitz company limited
# Created on: 2018-11-13 17:34:25.00000
# ---------------------------------------------------------------------------
import requests

url = "http://data.tmd.go.th/api/WeatherToday/V1/"

payload = ""
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "keys"
    }

response = requests.request("GET", url, data=payload, headers=headers)

#print(response.text)
data = response.json()
#print(type(data))
dict_1=data
#print(data.keys())
#print(data['Stations'])
#print(type(dict_1['Stations']))
#print(len(dict_1['Stations']))
#print(dict_1['Stations'])
#print(dict_1['Stations'][0])
#print(dict_1['Stations'][0].keys())
#print(dict_1['Stations'][0]['Observe'].keys())
#print(dict_1['Stations'][0]['Observe']['Rainfall'])
#print(dict_1['Stations'][0]['Observe']['Rainfall'].keys())
#print(dict_1['Stations'][0]['Observe']['Rainfall']['Value'])
#print(dict_1['Stations'][0]['Observe']['Temperature']['Value'])
#list_branch_name=[]
#for item in dict_1['Stations']:
#    list_branch_name.append(item['StationNameTh'])
#print(list_branch_name)
import pandas as pd
df1 = pd.DataFrame()
list_branch_name=[]
for item in dict_1['Stations'] :
            list_branch_name.append(item['StationNameTh'])
df1['name']=list_branch_name

list_lat=[]
for item in dict_1['Stations'] :
            list_lat.append(item['Latitude'])
df1['lat'] = list_lat

list_long=[]
for item in dict_1['Stations'] :
           list_long.append(item['Longitude'])
df1['long'] = list_long

list_Rain=[]
for item in dict_1['Stations'] :
           list_Rain.append(item['Observe']['Rainfall']['Value'])
df1['rain'] = list_Rain

list_Temp=[]
for item in dict_1['Stations'] :
           list_Temp.append(item['Observe']['Temperature']['Value'])
df1['temp'] = list_Temp

print(df1)
df1.to_csv('bbbb.csv')