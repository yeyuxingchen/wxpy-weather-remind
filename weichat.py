#!/usr/bin/python36
# -*- coding: utf-8 -*-
from wxpy import *
import json

name = ''

#auto
def join_wechat():
	#itchat.auto_login(hotReload=True)
	#itchat.auto_login(enableCmdQR=2)
	bot = Bot(cache_path=True)
	bot.file_helper.send('Hello wechat join success!')
	return bot

def push_massage(friend,str):
	friend.send(str[0] + str[1] + str[2])

def search_friend(bot,friend_name='独孤伶俜小'):
	friend = bot.friends().search(name)[0]
	return friend

def get_weather_jian():
	file = open("/home/pi/git-code/wechat/weather_jian.json", "r")
	strj = json.load(file)
	file.close()
	return strj

def get_user_json():
	file = open("/home/pi/git-code/wechat/user.json", "r")
	userj = json.load(file)
	file.close()
	return userj

userj =  get_user_json()
str = get_weather_jian()
bot = join_wechat()
for city in userj['city']:
        weather_jian = str[city]['s1'] + str[city]['s2'] + '\n独小酱祝您晚安 好梦！\n\n这是一条由python程序发送的消息，请不要回复!\n ——独孤伶俜'
        #weather_jian = '今天是6月1日儿童节哦～独小酱买了一斤糖果哦～' + '\n独小酱再次祝您晚安 好梦！\n\n这是一条由python程序发送的消息，请不要回复!\n ——独孤伶俜'
        print(city)
        #print(weather_jian)
        for name in userj[city]['user']:
                print(name)
                friend = bot.friends().search(name)[0]
                friend.send(weather_jian)


