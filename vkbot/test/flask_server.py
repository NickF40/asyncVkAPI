from flask import Flask
import json
import vkbot
import vk

# Consts
confirmation_token = ""
token = ''

app = Flask(__name__)
bot = vkbot.VkBot(token)

"""
Request example:
 {
 "type":"message_new",
 "object":{"id":43, "date":1492522323, "out":0, "user_id":xxxxxxxx, "read_state":0, "title":" ... ", "body":"помощь"},
 "group_id":xxxxxxxxxxx
 }

"""


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return
    if data['type'] == 'confirmation':
        return confirmation_token
    else:
        bot.process_new_updates(data)
