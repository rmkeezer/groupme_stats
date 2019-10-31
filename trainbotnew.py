# -*- coding: utf-8 -*-

from chatterbot import ChatBot
import sys
import pandas as pd
import numpy as np

df = pd.read_csv('flouricao.csv')
data = df.values

target = "Christian Fuchs"
chatbot = ChatBot(
    target,
    trainer='chatterbot.trainers.ListTrainer'
)

# convs = []
# statement = ''
# response = True
# for x in data:
#     if x[2] != target:
#         response = True
#         statement = x[3]
#     if response and x[2] == target and len(str(x[3])) > 1:
#         convs.append(statement)
#         convs.append(x[3])
#         #chatbot.train([statement, x[3]])
#         response = False
# chatbot.train(convs)

print("DONE")
print(chatbot.get_response("Hello, how are you today?"))
print(chatbot.get_response("test"))
print(chatbot.get_response("yo"))
print(chatbot.get_response("it is wednesday my dudes"))
print(chatbot.get_response("it's thirsty thursday boyos"))

# import requests
# msg = chatbot.get_response("it is wednesday my dudes")
# msg = str(msg)
# print(msg)
# msg.replace(" ", "+")
# response = requests.post(
#     url="https://api.groupme.com/v3/bots/post?bot_id=1dfc618d351724d61d8585f9c4&text=" + msg)
# print(response.status_code, response.reason)