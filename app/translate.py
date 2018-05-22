import hashlib
import json
import random
import urllib

import requests
from flask import current_app


def translate(text, source_language, desc_language):
    q = text
    fromLang = source_language
    toLang = desc_language
    appId = current_app.config['BAIDU_TRANS_APPID']
    appKey = current_app.config['BAIDU_TRANS_KEY']
    salt = random.randint(32768, 65536)
    salt = '1'

    sign = appId + q + str(salt) + appKey
    sign = hashlib.md5(sign.encode('utf-8')).hexdigest()

    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    url = url + '?q=' + urllib.request.quote(q) + '&from=' + fromLang + \
        '&to=' + toLang + '&appid=' + appId + '&salt=' + salt + '&sign=' + sign

    r = requests.get(url)

    if r.status_code != 200:
        print('Translate Error')
        return 'Error: the translate service failed'
    print(json.loads(r.content.decode('utf-8')))
    return json.loads(r.content.decode('utf-8'))
