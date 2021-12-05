# slackapp
A tool which implements /afk slack command

# Development

## grok

Need proxy to talk to help Slack to talk to your app
Register on ngrok.com and get the <token> from https://dashboard.ngrok.com/get-started/setup

Install grok

```
❯ sudo tar xvzf ~/Downloads/ngrok-stable-linux-amd64.tgz -C /usr/local.
❯ ngrok authtoken <token>
❯ ngrok http 3000
```

## Slack App tokens
Now the only thing is missing is SLACK_BOT_TOKEN and SLACK_SIGNING_SECRET. for them we have to go to https://api.slack.com/apps and create an App and install it on your _Workspace_ which you chose to use for the app.
Then on *OAuth & Permissions* will fetch `Bot User OAuth Token` and from *Basic Information* will find *App Credentials* and *Client Secret*

```
export SLACK_BOT_TOKEN=xoxb-<OAuth_Token>
export SLACK_SIGNING_SECRET=<secret_token>
```

## install venv to host the service which Slack will talk to

make a virtualenv and install dependencies

```
❯ pip install -r requirements.txt
❯ python app.py
INFO:slack_bolt.App:⚡️ Bolt app is running! (development server)
```


## Examples

_/afk i will be away for 1h_
_/afk list_
_/afk del_
