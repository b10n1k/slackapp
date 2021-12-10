import os
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
from slack_bolt import App, Ack, Say
from slack_sdk import WebClient
from slack_sdk.web import SlackResponse
import time

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)
afkers = {}

@app.command("/afk")
def handle_request(body, client, ack, logger):
    global afkers
    ack()
    say  = Say(client, body['channel_id'])
    t = time.localtime()
    logger.info(body)
    if body['text'] != '':
        if body['text'].startswith('list'):
            ack()
            logger.info("Get afkers list")
            display_afk(say)
        if body['text'].startswith('del'):
            ack()
            remove_afk(say, body['user_name'])
            logger.info("%s change his status!" % body['user_name'])
        else:
            ack("I got it! %s" % str(afkers))
            logger.info("%s change his status!" % body['user_name'])
            newafk = {}
            newafk['note'] = body['text']
            newafk['since'] = t
            afkers[body['user_name']] = newafk

def display_afk(say):
    outp = ''
    for user, data in afkers.items():
        htime = time.asctime(data['since'])
        outp += "%s : %s \t'%s'\n" % (htime, user, data['note'])
    say(outp)

def remove_afk(say, user):
    del afkers[user]
    say("%s is on-screen\n" % user)

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
