[![Latest Version](https://img.shields.io/pypi/v/discord-msg-lite.svg)](https://pypi.org/project/discord-msg-lite/)

# Discord message lite

This is a simple and lightweight Python PyPI module to send messages easily using Discord Webhooks.

## Installation

Run the following to install:

```python
pip install discord-msg-lite
```

## Usage

```python
from discord_msg_lite import Discord_msg

webhook_url = 'https://discordapp.com/api/webhooks/123456789012345678/8xZhP4Zj-8KMVN7wLw6jE04VEK5BIfRxpzCwCwgHxpaNOQzZOTR95dPW53EMRjybXjAO'
dmsg = Discord_msg(webhook_url)
dmsg.send('test 12345 ㄱㄴㄷㄹ')
```
