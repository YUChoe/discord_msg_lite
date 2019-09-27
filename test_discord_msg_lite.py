from src.discord_msg_lite import Discord_msg
import time

def test_send():
    webhook_url = 'https://discordapp.com/api/webhooks/627020063651790858/8hxP4ZZj-8KMw6jE04VEK5BIfRxpz53VN7wLEMCwCwgHxpZOTR95dPWRjybaNOQzXjAO'
    dmsg = Discord_msg(webhook_url)
    assert dmsg.send('test 12345 ㅁㄴㅇㄹ at {}'.format(time.asctime())) == ''
