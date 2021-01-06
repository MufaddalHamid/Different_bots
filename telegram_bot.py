# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:28:38 2021

@author: Mufaddal Hamid
"""
#import schedule
import requests


def telegram_bot_sendtext(bot_message):
    
    bot_token = ' bot_token'
    bot_chatID = 'bot_chat_id'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' +"message"

    response = requests.get(send_text)

    return response.json()


def report():
    my_balance = 500   ## Replace this number with an API call to fetch your account balance
    my_message = "Current balance is: {}".format(my_balance)   ## Customize your message
    js=telegram_bot_sendtext(my_message)
    print(type(js))
def getchat_id():
     bot_token = ' bot_token'
    # bot_chatID = '14826629'
     up='https://api.telegram.org/bot'+bot_token+'/getUpdates'
     res=requests.get(up)
     js=res.json()
     chat_id=js['result'][2]['message']['chat']['id']
     text=js['result'][len(js['result'])-1]['message']['text']
     print(chat_id,"------",text)
    
getchat_id()
report()
    
#schedule.every().day.at("12:00").do(report)

#while True:
 #   schedule.run_pending()
  #  time.sleep(1)
