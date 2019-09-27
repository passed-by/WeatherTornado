# urls.py: 存放路由配置
from tornado.web import url
from App.views import *

patterns = [

    url(r'/weather/', WeatherIndex),
    url(r'/weatherinfo/', WeatherHandler, name="wea"),

]

