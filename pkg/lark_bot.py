# coding: utf-8

import functools
import requests
import traceback
from loguru import logger

__data = {}

def init_with_webhook(webhook: str):
    if webhook:
        __data['webhook'] = webhook


def send_msg(msg: str):
    if 'webhook' not in __data:
        logger.warning('lark not not inited')
        return

    payload = {
        'msg_type': 'text',
        'content': {
            'text': msg,
        }
    }
    
    requests.post(__data['webhook'], json=payload)


def exception_notify(fn):

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            notify_msg = f'{e}\n{traceback.format_exc()}'
            send_msg(notify_msg)
            raise e

    return wrapper
