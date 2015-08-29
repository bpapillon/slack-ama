from flask import abort, Flask, request
from os import environ as env
from slacker import Slacker
from sys import argv

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
        return "Question submitted!"
    return "What's your question?"

if __name__ == '__main__':
    kwargs = {'host': '0.0.0.0'}
    if len(argv) > 1:
        kwargs['port'] = int(argv[1])
    app.run(**kwargs)
