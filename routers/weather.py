from fastapi import APIRouter, Request
import weather_controller as controller
from pydantic import BaseModel

class WeatherCurrent(BaseModel):
    t: str = None
    h: str = None
    d: str = None
    p: str = None
    s: str = ''

weather_path = '/api/weather'
weather = APIRouter()

##################### weather data
@weather.get(weather_path + '/temphumidity/current')
def temphumidity_get_current(output: str = ''):
    if (output.lower()) == 'xml':
        return controller.get_currentXML()
    return controller.get_current()

@weather.get(weather_path + '/forecast')
def forecast_handler():
    return controller.get_latest_forecast()
@weather.get(weather_path + '/history/barometerHumidity')
def history_barometer_humidity_handler():
    return controller.get_barometer_history()

@weather.get(weather_path + '/settings/timezone')
def settings_timezone_handler(request: Request):
    return controller.get_timezone(request)
@weather.get(weather_path + '/settings/timezone-list')
def settings_timezone_list_handler():
    return controller.get_timezone_list()
@weather.get(weather_path + '/settings/timezone_async')
async def settings_timezone_handler_async(request: Request):
    await controller.get_settings_timezone_async(request)

@weather.post(weather_path + '/temphumidity/add')
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

    
   