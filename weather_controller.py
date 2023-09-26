from fastapi import Request, Response
from dicttoxml import dicttoxml
from pydantic import BaseModel
import db
import datetime

    
def get_current():
    conn = db.open()
    cursor = conn.cursor()
    query = ("select recorded_time,temp,humidity,"
            " (SELECT temp FROM weather_data WHERE recorded_time < DATE_ADD(w.`recorded_time`, INTERVAL -30 MINUTE) ORDER BY recorded_time DESC, source LIMIT 1) AS recent_temp, source,"
            " (SELECT temp FROM weather_data WHERE source = 'web' AND recorded_time >= DATE_ADD(w.`recorded_time`, INTERVAL -10 MINUTE) ORDER BY recorded_time DESC LIMIT 1) AS temp_web,"
            " (SELECT humidity FROM weather_data WHERE source = 'web' AND recorded_time >= DATE_ADD(w.`recorded_time`, INTERVAL -10 MINUTE) ORDER BY recorded_time DESC LIMIT 1) AS humidity_web,"
            " (SELECT pressure FROM weather_data WHERE source = 'web' AND recorded_time >= DATE_ADD(w.`recorded_time`, INTERVAL -10 MINUTE) ORDER BY recorded_time DESC LIMIT 1) AS pressure_web"
            " FROM weather_data w order by recorded_time desc, source limit 1;")
    cursor.execute(query)
    respObj = {}
    respObj["status"]="ok"
    dataObj = []

    for (var_recorded_time, var_temp, var_humidity, var_recent_temp, var_source, var_temp_web, var_humidity_web, var_pressure_web) in cursor:
        print("time: {}, temp: {}, humidity: {}, recent temp: {}, web temp: {}".format(
        var_recorded_time, var_temp, var_humidity, var_recent_temp, var_temp_web, var_humidity_web))
        dataItem={}
        dataItem["recorded_time"]=str(var_recorded_time)
        dataItem["temp"]=str(var_temp)
        dataItem["humidity"]=str(var_humidity)
        dataItem["recent_temp"]=str(var_recent_temp)
        dataItem["source"] = var_source
        dataItem["temp_web"] = str(var_temp_web)
        dataItem["pressure_web"] = str(var_pressure_web)
        dataItem["humidity_web"] = str(var_humidity_web)
        dataObj.append(dataItem)

    respObj["data"]=dataObj
    cursor.close()
    conn.close()
    return respObj
def get_currentXML():
    resp = dicttoxml(get_current())
    return Response(content=resp, media_type="application/xml")
def get_barometer_history():
    daysBack = 3
    conn = db.open()
    cursor = conn.cursor()
    args = [daysBack]
    cursor.callproc('api_get_barometer_data', args)
    rows = cursor.fetchall()
    respObj={}
    respObj["status"]="ok"
    dataObj=[]
    for row in rows:
        var_date=row[0]
        var_barometer=row[1]
        var_humidity=row[2]
        dataItem={}
        dataItem["timeStamp"]=str(var_date)
        dataItem["barometer"]=var_barometer
        dataItem["humidity"]=var_humidity        
        dataObj.append(dataItem)
    respObj["data"]=dataObj
    cursor.close()
    conn.close()
    return respObj
    
def get_latest_forecast():
    currentDT = str(datetime.datetime.now())
    conn = db.open()
    cursor = conn.cursor()
    #query =("CALL api_get_forecast_data(%s);")
    #cursor.execute(query,(currentDT))
    args = [currentDT]
    cursor.callproc('api_get_forecast_data', args)
    print(cursor.fetchone);
    rows = cursor.fetchall()
    respObj={}
    respObj["status"]="ok"
    dataObj=[]
    for row in rows:
        var_forecast_date=row[0]
        var_forecast_data=row[1]
        dataItem={}
        dataItem["forecast_date"]=str(var_forecast_date)
        dataItem["forecasts"]=var_forecast_data
        dataObj.append(dataItem)

    respObj["data"]=dataObj
    cursor.close()
    conn.close()
    return respObj
def get_settings_timezone(response):
    zone=response.zone
    respObj = {}
    respObj["zone"] = zone
    return  respObj
def add(request):

    temp = request.t
    humidity = request.h
    time = request.d
    pressure = request.p
    source = request.s
    lastrowid = -1
    conn = db.open()
    cursor = conn.cursor()
    query = ("insert into weather_data " 
            "(recorded_time, temp, humidity, pressure, source)"
            " select %s, %s, %s, %s, %s;"
           )
    
    cursor.execute(query,(time, temp, humidity, pressure, source))
    conn.commit()
    lastrowid = cursor.lastrowid
    
    cursor.close()
    conn.close()

    respObj = {}
    respObj["status"]="ok"
    dataObj = {}
    dataObj["id"] = lastrowid
    respObj["data"] = dataObj
    print('weather_controller.add:', respObj)
    return  respObj

def delete(data):
    return '{"status":"failed", "err":"not implemented","data":[]}'
    