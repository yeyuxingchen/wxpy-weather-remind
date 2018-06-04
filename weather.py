#!/usr/bin/python3.6
#-*-coding:utf-8 -*-
import requests
import json
import time

juheurl = 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname='	#这里是聚合数据api 你需要申请一个key
freeurl = 'https://www.sojson.com/open/api/weather/json.shtml?city='
date = time.strftime('%Y%m%d',time.localtime(time.time()))
file = open("user.json", "r")
userj = json.load(file)
file.close()

file = open("weather.json", "r")
jsonj = json.load(file)
file.close()

def get_weather_json(userj,jsonj,date):
    for city in userj['city']:
        print(city)
        if (jsonj[city]['date'] == date and jsonj[city]['code'] == '200'):
            print('不需要重新请求 今天：' + date + city)
            continue
        jsonAPI = requests.get(userj[city]['freeurl'])
        jsonAPI.encoding = 'utf-8'
        jsonj[city] = jsonAPI.json()
        if jsonj[city]['status'] == 200:
            jsonj[city]['url_type'] = 'free'
            jsonj[city]['date'] = date
            jsonj[city]['city'] = city
            jsonj[city]['code'] = str(jsonj[city]['status'])
        else:
            jsonAPI = requests.get(userj[city]['juheurl'])
            jsonAPI.encoding = 'utf-8'
            jsonj[city] = jsonAPI.json()
            if (jsonj[city]['resultcode'] == '200'):
                jsonj[city]['url_type'] = 'juhe'
                jsonj[city]['date'] = date
                jsonj[city]['city'] = city
                jsonj[city]['code'] = str(jsonj[city]['resultcode'])
                #写入文件
            else:
                jsonj[city]['url_type'] = 'error'
                jsonj[city]['date'] = date
                jsonj[city]['city'] = city
                jsonj[city]['code'] = str(jsonj[city]['resultcode'])
        time.sleep(3)   #程序控制流程睡眠3秒
    jsonj['city'] = userj['city']
    file = open("weather.json", "w")
    file.write(json.dumps(jsonj))
    file.close()
    return jsonj

wea = get_weather_json(userj,jsonj,date)
#print("\n\n\n")
print(wea)
