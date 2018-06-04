#!/usr/bin/python36
# -*- coding: utf-8 -*-

import json

user = {'西青' : ['独孤伶俜小','段仁伟','吴小岩','王超','雷静','刘洪哲','王世新'],
	'酒泉' : ['独孤伶俜小','姑姑','大妈','奶奶','囯舅','大伯忠宁'],
	'敦煌' : ['妈妈','爸爸'],
	'郑州' : ['张毅'],
	'武汉' : ['周思雨'],
	'连云港' : ['刘海森'],
	't' : ['独孤伶俜小','独孤伶俜小']
}

userj = {'city': ['西青', '武汉','酒泉','郑州','敦煌','连云港'], 
		'西青' : {'user': ['独孤伶俜小','段仁伟','吴小岩','王超','雷静','刘洪哲','王世新'], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=西青', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=西青'
		}, 
		'武汉' : {'user': ['独孤伶俜小','周思雨'], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=武汉', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=武汉'
		},
		'酒泉' : {'user': ['独孤伶俜小','姑姑','大妈','奶奶','大伯忠宁'],
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=酒泉', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=酒泉'
		}, 
		'郑州' : {'user': ['独孤伶俜小', '张毅'], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=郑州', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=郑州'
		}, 
		'敦煌' : {'user': ['妈妈','爸爸'], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=敦煌', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=敦煌'
		},
		'连云港' : {'user': ['刘海森'], 
			'juheurl': 'http://v.juhe.cn/weather/index?key=812c24622ff48c957dc025e2030d16f7&cityname=连云港', 
			'freeurl': 'https://www.sojson.com/open/api/weather/json.shtml?city=连云港'
		},
	}
print(userj)
file = open("user.json", "w")
file.write(json.dumps(userj))
file.close()
