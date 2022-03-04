# coding: utf-8

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from calc import *
import os

class class1(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("User-Agent","test1")
        self.end_headers()
        # 折角なので計算もさせる
        html = "<h1>Answer is " + str(mul(6,7)) +  "</h1>"
        self.wfile.write(html.encode())

ip = '0.0.0.0'
# PORTという環境変数からherokuが割り当てたポート番号を取得する
port = int(os.environ.get('PORT', 8765)) 

server = HTTPServer((ip, port), class1)
print("Access http://0.0.0.0:" + str(port))
server.serve_forever()


