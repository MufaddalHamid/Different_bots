# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:33:32 2021

@author: LENOVO
"""
import discord
import os
import nest_asyncio
import requests
import json
import random
nest_asyncio.apply()
#from replit import db
import random

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]
db={"encouragement":starter_encouragements}
def quote():
    resp=requests.get("https://zenquotes.io/api/random")
    js_data=json.loads(resp.text)
    q=js_data[0]['q']+"-"+js_data[0]['a']
    return q


client = discord.Client()
def encouragement(en_ms):
  if "encouragement" in db.keys():
    emc=db["encouragement"]
    emc.append(en_ms)
    db["encouragement"]=emc
  else:
    db["encouragement"]=[en_ms]

def dele_msg(index):
  emc=db["encouragement"]
  if len(emc)>index:
    del emc[index]
  db["encouragement"]=emc

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$inspire'):
        q=quote()
        await message.channel.send(q)
    if any(wrd in msg for wrd in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
    if msg.startswith('@add'):
      val=msg.split('@add',1)[1]
      encouragement(val)
      await message.channel.send("message added bruh")
    if msg.startswith('@del'):
      emc=[]
      val=int(msg.split('@del',1)[1])
      if "encouragement" in db.keys():
        dele_msg(val)
        emc=db["encouragement"]
        await message.channel.send(emc)        

client.run('Your Token here after creating bot on website')
