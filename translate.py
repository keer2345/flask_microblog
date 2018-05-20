import json
import md5
import random
import urllib

import requests

from app import app


def translate(text, source_language, desc_language):
    q = text
    fromLang = source_language
    toLang = desc_language
    appId = app.config['BAIDU_TRANS_APPID']
    appKey = app.config['BAIDU_TRANS_KEY']
    salt = random.randint(32768, 65536)

    sign = appId + q + str(salt) + appKey
    sign = md5.new().update(sign)

    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    url = url + '?q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + \
        toLang + '&appid=' + appId + '&salt=' + salt + '&sign=' + sign

    r = requests.get(url)

    if r.status_code != 200:
        print('Translate Error')
        return 'Error: the translate service failed'
    return json.loads(r.content.decode('utf-8'))
