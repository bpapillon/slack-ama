from flask import abort, Flask, request
from os import environ as env
from slacker import Slacker

app = Flask(__name__)
slack = Slacker(env.get('SLACK_API_TOKEN'))

@app.route('/question', methods=['POST'])
def question():
    valid_token = env.get('SLACK_COMMAND_TOKEN')
    if valid_token:
        request_token = request.form.get('token')
        if request_token != valid_token:
            abort(401)
    channel = env.get('SLACK_CHANNEL')
    text = request.form.get('text')
    if text:
        slack.chat.post_message(channel, text)
    return 'ok'

if __name__ == '__main__':
    app.run()
