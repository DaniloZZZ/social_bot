
from pytg import Telegram
from pytg.utils import coroutine
import logging

tg = None
def init(tg_cli, pubkey_file):
    global tg
    tg = Telegram(
            telegram=tg_cli,
            pubkey_file=pubkey_file
    )
    receiver = tg.receiver
    sender = tg.sender
    l = sender.contacts_list()
    return tg

def send(username, text):
    logging.debug(f">>> {username}::{text}")
    tg.sender.send_msg(username, text)

@coroutine
def _loop(callback):
    while True:
        msg = (yield)
        logging.debug(f"<<< {msg}")
        callback(msg)
def listener(callback):
    """
    """
    tg.receiver.start()
    tg.receiver.message(_loop(callback))

def history(usr, limit=10, offset=0):
    logging.debug(
        f"History from {usr}, limit:offset={limit}:{offset}")
    return tg.sender.history(usr,limit,offset)
