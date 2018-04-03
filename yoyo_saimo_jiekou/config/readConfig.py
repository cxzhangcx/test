



import os
import configparser
import re

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "cfg.ini")
conf = configparser.ConfigParser()
# print(configPath)

conf.read(configPath,'utf_8')

smtp_server = conf.get('email', 'smtp_server')

sender = conf.get("email", "sender")

psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver")

port = conf.get("email", "port")
