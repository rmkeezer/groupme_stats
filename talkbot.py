# -*- coding: utf-8 -*-

from chatterbot import ChatBot
import requests

target = "Christian Fuchs"
chatbot = ChatBot(
    target,
    trainer='chatterbot.trainers.ListTrainer'
)

msg = chatbot.get_response("praise johan")
msg = str(msg)
print(msg)
msg.replace(" ", "+")
response = requests.post(
    url="https://api.groupme.com/v3/bots/post?bot_id=1dfc618d351724d61d8585f9c4&text=" + msg)
print(response.status_code, response.reason)