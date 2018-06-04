#!/usr/bin/python3.6
#-*-coding:utf-8 -*-
import requests
import json
import time

userj = {'city': ['西青', '武汉','酒泉','郑州','敦煌'], 
		'西青': {'user': ['独孤伶俜小', '段仁伟', ], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=西青', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=西青'
		}, 
		'武汉': {'user': ['独孤伶俜小',], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=武汉', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=武汉'
		},
		'酒泉': {'user': ['独孤伶俜小', ], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=酒泉', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=酒泉'
		}, 
		'郑州': {'user': ['独孤伶俜小', ], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=郑州', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=郑州'
		}, 
		'敦煌': {'user': ['独孤伶俜小', ], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=敦煌', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=敦煌'
		},
	}

'''
cishu = 0
juheurl = 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname='	#这里是聚合数据api 你需要申请一个key
freeurl = 'https://www.sojson.com/open/api/weather/json.shtml?city='

file = open("user.json", "r")
userj = json.load(file)
file.close()
#print(userj)
print("plase input your city:")
newcity = input()
print("plase input your city:")
newname = input()
for city in userj['city']:
    if newcity == city:
        for name in userj[city]['user']:
            if newname == name:
                print(1)
                continue
            else:
                userj[city]['user'].append(newname)
                print(12)
                break
'''
print(userj)
file = open("user.json", "w")
file.write(json.dumps(userj))
file.close()
