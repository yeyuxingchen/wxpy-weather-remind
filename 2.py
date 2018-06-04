import json
import time

def get_weather_json(jsonj):
	date = time.strftime('%Y%m%d',time.localtime(time.time()))
	weather = {'city' : jsonj['city']}
	for city in jsonj['city']:
		print(city)
		if (jsonj[city]['date'] == date):
			if jsonj[city]['url_type'] == 'juhe':
				weather[city] = {
					'code' : '200',
					'date' : jsonj[city]['date'],
					'url_type' : jsonj[city]['url_type'],
					'city' : jsonj[city]['result']['today']['city'],
					'aqi' : jsonj[city]['result']['today']['comfort_index'],
					'weather_info' : jsonj[city]['result']['today']['temperature'],
					'fengli' : jsonj[city]['result']['today']['wind'],
					'type' : jsonj[city]['result']['today']['weather'],
					'qingkuang' : jsonj[city]['result']['today']['dressing_index'],
					'notice' : jsonj[city]['result']['today']['dressing_advice']
				}
		
			elif jsonj[city]['url_type'] == 'free':
				weather[city] = {
					'date' : jsonj[city]['date'],
					'url_type' : jsonj[city]['url_type'],
					'city' : jsonj[city]['city'],
					'shidu' : jsonj[city]['data']['shidu'],
					'aqi' : jsonj[city]['data']['forecast'][0]['aqi'],
					'high' : jsonj[city]['data']['forecast'][0]['high'],	
					'low' : jsonj[city]['data']['forecast'][0]['low'],
					'fengxiang' : jsonj[city]['data']['forecast'][0]['fx'],
					'fengli' : jsonj[city]['data']['forecast'][0]['fl'],
					'type' : jsonj[city]['data']['forecast'][0]['type'],
					'notice' : jsonj[city]['data']['forecast'][0]['notice']
				}
			else:
				weather[city] = {
					'date' : jsonj[city]['date'],
					'url_type' : jsonj[city]['url_type'],
					'errorinfo' : '哎呀，出错啦！可能是城市输入错误。'
				}
		else:
			weather[city] = {
				'date' : jsonj[city]['date'],
				'url_type' : jsonj[city]['url_type'],
				'errorinfo' : "哎呀，天气数据过期啦，请重新获取。"
				}
	return weather


def read_json_file():
	file = open("weather.json", "r")
	jsonj = json.load(file)
	file.close()
	#print(jsonj)
	return jsonj

def write_json_file(jsonj):
	file = open("weather_jian.json", "w")
	file.write(json.dumps(jsonj))
	file.close()

def get_weather_info(weather):
	str = {'city' : weather['city']}
	for city in weather['city']:
		if weather[city]['url_type'] == 'free':
			timeclock = time.strftime('今天是%m月%d日，',time.localtime(time.time()))
			temp = timeclock + '今天' + weather[city]['city'] + weather[city]['type']+',' + weather[city]['high'] + '，'+weather[city]['low']+'，'+weather[city]['fengxiang']+weather[city]['fengli']
			str[city] = [temp,]
			temp = "湿度: %s,天气质量:%s。%s" % (weather[city]['shidu'],weather[city]['aqi'],weather[city]['notice'])
			str[city].append(temp)
		elif weather[city]['url_type'] == 'juhe':
			#juhe
			timeclock = time.strftime('今天是%m月%d日，',time.localtime(time.time()))
			str[city] = [(timeclock + '今天' + weather[city]['city'] + weather[city]['type']+ ',温度：'+ weather[city]['weather_info'] + ',' +weather[city]['fengli']),]
			str[city].append(('今天天气' + weather[city]['qingkuang'] +'。' + weather[city]['notice']))
		else:
			timeclock = time.strftime('今天是%m月%d日，',time.localtime(time.time()))
			str[city] = [timeclock,]
			str[city].append(weather[city]['errorinfo'])
	return str

def main():
	weatherjosn = read_json_file()
	#print(weatherjosn)
	weather = get_weather_json(weatherjosn)
	#print(weather)
	str = get_weather_info(weather)
	#print(str)
	for city in weather['city']:
		weather[city]['s1'] = str[city][0]
		weather[city]['s2'] = str[city][1]
		#print(weather)
		print(weather[city]['s1'],weather[city]['s2'])
	write_json_file(weather)
if __name__ == '__main__':
	main()

