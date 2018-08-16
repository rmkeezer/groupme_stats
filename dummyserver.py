#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

from chatterbot import ChatBot
import requests

import random

target = "Christian Fuchs"
chatbot = ChatBot(
    target,
    trainer='chatterbot.trainers.ListTrainer'
)

hostName = ""
hostPort = 5000

class MyServer(BaseHTTPRequestHandler):

    #	GET is for clients geting the predi
    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))

    #	POST is for submitting data.
    def do_POST(self):

        print( "incomming http: ", self.path )

        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(content_length)
        print(post_data)
        data = json.loads(post_data.decode('utf8'))
        if 'fuchs' in data['name'].lower() or '!' in data['text'][:5]:
            self.send_response(200)
            return
        trigs = ["bjck", "OOPSIE WOOPSIE!! Uwu We made a fucky wucky!! A wittle fucko boingo! The code monkeys at our headquarters are working VEWY HAWD to fix this!".lower()]
        if random.random() < 0.9 and all(x not in data['text'].lower() for x in trigs):
            self.send_response(200)
            return
        msg = chatbot.get_response(data['text'])
        msg = str(msg)
        resps = ["markov", "@"]
        if all(x not in msg for x in resps):
            msg = '@' + data['name'] + ' ' + msg
        print(msg)
        msg.replace(" ", "+")
        print("START POST")
        response = requests.post(
            url="https://api.groupme.com/v3/bots/post?bot_id=4081375711b06614af16500b07&text=" + msg, verify=False)
        print("END POST")
        print(response.status_code, response.reason)
        self.send_response(200)

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
