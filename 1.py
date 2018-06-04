# coding: utf-8
from wxpy import *
bot = Bot(cache_path=True)
# 初始化图灵机器人 (API key 申请:http://www.tuling123.com/)
tuling = Tuling(api_key='927d9e67b4c24f67a8b11a5daa93d0dc')
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)
bot.join()