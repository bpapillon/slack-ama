from dotenv import load_dotenv
from flask import Flask, request
from os import environ as env
from slacker import Slacker

app = Flask(__name__)
load_dotenv('.env')
slack = Slacker(env.get('SLACK_API_TOKEN'))


@app.route('/question', methods=['POST'])
def question():
    channel = env.get('SLACK_CHANNEL')
    text = request.form.get('text')
    if text:
        slack.chat.post_message(channel, text)


if __name__ == '__main__':
    app.run()
