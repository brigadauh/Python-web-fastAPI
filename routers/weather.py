from fastapi import APIRouter, Request
import weather_controller as controller
from pydantic import BaseModel

class WeatherCurrent(BaseModel):
    t: str = None
    h: str = None
    d: str = None
    p: str = None
    s: str = ''

path = '/api/weather/temphumidity'
weather = APIRouter()

##################### weather data
@weather.get(path + '/current')
def temphumidity_get_current(output: str = ''):
    if (output.lower()) == 'xml':
        return controller.get_currentXML()
    return controller.get_current()

@weather.get('/api/weather/forecast')
def forecast_handler():
    return controller.get_latest_forecast()
@weather.get('/api/weather/history/barometerHumidity')
def history_barometer_humidity_handler():
    return controller.get_barometer_history()

@weather.post('/api/weather/temphumidity/add')
def temphumidity_add(request: WeatherCurrent):
    # print('request--------->:', request.json())
    # print('temp--------->:', request.t, request.h, request.d, request.p, request.s)
    return controller.add(request)






    # @app.delete('/api/weather/temphumidity/add')
    # def temphumidity_handler_process():
    #     return temphumidity.add()
    # 

    # 
    # @app.route('/api/weather/forecast', methods=['POST','GET'])
    # def forecast_handler():
    #     return forecast.get_latest()

    
   