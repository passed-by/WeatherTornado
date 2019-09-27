import json

import requests

# Request：
# Url: http://characters.market.alicloudapi.com/ln/report/mastercode/emotion_description/1.0
# Header = {
#       "Host":"characters.market.alicloudapi.com",
#       "X-Ca-Timestamp":"1567772718037",
#       "gateway_channel":"http",
#       "X-Ca-Request-Mode":"debug",
#       "X-Ca-Key":"203740981",
#       "X-Ca-Stage":"RELEASE",
#       "x-ca-nonce":"c6529f8c-c6ea-4f78-bf18-7e3792d00ef0",
#       "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
#       "Authorization":"APPCODE 7b9862e5b4bc4906a1d6f87e0f417ebd"
# }
# Body: {"birthday":"19970912"}


# {"masterCode":2,
# "description":"2号性格的人天生敏感、擅长分析，他们的对照和比较能力都较其他人突出很多。
# 他们也喜欢和别人亲密相处，但又因为很敏感，很喜欢分析对方的态度，所以往往会对别人的表现产生诸多不满，
# 如果他们把自己的这种感觉说出来，就会给人一种喜欢批评别人的感觉。
# 因此在爱情关系方面，2号性格的人，他们的感情较为热切而强烈，却又极富情绪化。热衷于亲密关系，
# 又因敏感而容易挑剔对方，这使得对方很有压力，并且做出逃避的决定，而他们一旦感觉自己受到拒绝，又会变得非常沮丧，
# 甚至一蹶不振。"}

url = 'http://saweather.market.alicloudapi.com/day15'

Header = {
    "Authorization": "APPCODE 7b9862e5b4bc4906a1d6f87e0f417ebd",
    "Type":"application/json; charset=utf-8",
}
#


def parse_city(city, days):
    payload = {'area': '{}'.format(city)}

    response = requests.get(url, params=payload, headers=Header)
    cityinfo_dict = json.loads(response.content)
    print(cityinfo_dict)
    # city_name = city                         #城市名字
    # city_num = cityinfo_dict['areaid']       #城市id
    # city_dayList = cityinfo_dict['dayList']    #近十天天气
    # print(city_dayList[:10:])

    # 白天天气





if __name__ == '__main__':
    city_weather = input("输入查看城市:")
    day_num = input("输入查看几天后天气(0~10)/天:")
    parse_city(city_weather, day_num)