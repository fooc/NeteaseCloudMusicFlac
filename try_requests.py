#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
}


url = 'http://www.wsyyxz.com/e/search/index.php'
payload = {'keyboard':u'缘分一道桥', 'tempid': 1, 'classid': u'1,2,3,4,5,6,7,8,9,10,11,12', 'show': u'title,newstext,ftitle', 'Submit22': u'搜索'}
r = requests.post(url, data=payload, headers=HEADERS)

contents = r.text

print(contents)