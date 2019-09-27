from src.discord_msg_lite import Discord_msg
import time

def test_send():
    webhook_url = ''
    dmsg = Discord_msg(webhook_url)
    assert dmsg.send('test 12345 ㅁㄴㅇㄹ at {}'.format(time.asctime())) == ''
