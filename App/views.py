# views.py: 存放类视图
#   存放RequestHandler
import asyncio
import json
import random
import threading
import time
import datetime

import requests


# 类视图
# 首页
class WeatherIndex(tornado.web.RequestHandler):
    def get(self):
        self.render("weather.html")


class WeatherHandler(tornado.web.RequestHandler):

    def get(self):
        url = 'http://saweather.market.alicloudapi.com/day15'
        Header = {
            "Authorization": "APPCODE 7b9862e5b4bc4906a1d6f87e0f417ebd",
            "Type": "application/json; charset=utf-8",
        }

        # print("url:",url)
        city = self.get_argument("city")

        payload = {'area': '{}'.format(city)}
        response = requests.get(url, params=payload, headers=Header)
        cityinfo_dict = json.loads(response.content)['showapi_res_body']
        self.write(json.dumps(cityinfo_dict))
