#from flask import Flask
import requests
import json
from datetime import datetime
import time

SMHI_temp_latestHour = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/1/station/52350/period/latest-hour/data.json"
SMHI_rain_latestHour = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/7/station/52350/period/latest-hour/data.json"
SMHI_forecast = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/13.07/lat/55.6/data.json"
"""
https://opendata.smhi.se/apidocs/metobs
https://opendata.smhi.se/apidocs/metfcst

~Station~
Malmö = 52350
GET /api/version/{version}/parameter/{parameter}/station/52350/period/{period}/data.json

~Parameter~
1 = Lufttemperatur
2 = Lufttemperatur
3 = Vindriktning
4 = Vindhastighet
6 = Relativ Luftfuktighet
7 = Nederbördsmängd

"""
def EpochToDate(jobj):
    d = jobj["value"][0]['date']/1000
    t = datetime.fromtimestamp(d).strftime('%Y-%m-%d %H:%M:%S')
    return t

def StrToDate(string):
    dateStr = string[1:11] + ' ' + string[12:20]
    t = datetime.strptime(dateStr, '%Y-%m-%d %H:%M:%S')
    return t


def getRain():
    response = requests.get(SMHI_rain_latestHour)
    jobj = response.json()

    time = EpochToDate(jobj)
    value = jobj["value"][0]['value']
    return [time, value]

def getTemp():
    response = requests.get(SMHI_temp_latestHour)
    jobj = response.json()

    time = EpochToDate(jobj)
    value = jobj["value"][0]['value']
    return [time, value]

def getPercForecast(nbr):
    HoursInFuture = nbr
    Categories = ["No percipitation", "Snow", "Snow and rain", "Rain", "Drizzle", "Freezing rain", "Freezing drizzle"]
    
    response = requests.get(SMHI_forecast)
    jobj = response.json()
    
    ValidTime = StrToDate(json.dumps(jobj["timeSeries"][HoursInFuture]["validTime"]))
    PercentFrozen = json.dumps(jobj["timeSeries"][HoursInFuture]["parameters"][0]["values"][0])
    PercCat = json.dumps(jobj["timeSeries"][HoursInFuture]["parameters"][1]["values"][0])
    PercCat = Categories[int(PercCat)]
    Pmin = json.dumps(jobj["timeSeries"][HoursInFuture]["parameters"][2]["values"][0])
    Pmean = json.dumps(jobj["timeSeries"][HoursInFuture]["parameters"][3]["values"][0])
    Pmax = json.dumps(jobj["timeSeries"][HoursInFuture]["parameters"][4]["values"][0])

    return [ValidTime, Pmin, Pmean, Pmax, PercCat, PercentFrozen]
    
def getTempForecast(nbr):
    HoursInFuture = nbr
    response = requests.get(SMHI_forecast)
    jobj = response.json()
    ValidTime = StrToDate(json.dumps(jobj["timeSeries"][HoursInFuture]["validTime"]))
    Temp = json.dumps(jobj["timeSeries"][HoursInFuture]["parameters"][10]["values"])

    
    return [ValidTime, Temp]

