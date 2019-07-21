#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re
import requests
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'
}

search_url = 'http://tool.liumingye.cn/music/'


def download_song(song_url):
	r = requests.get(song_url, headers=HEADERS)
	contents = r.text

	# encoding problems of Chinese
	pattern = r'onclick="window.open\(\'(.+?)\',.+\x86ç\xa0\x81: (.+?)</div>'
	results = re.search(pattern, contents)
	url2 = results.group(1)
	passwd = results.group(2)

	r = requests.get(url2, headers=HEADERS)
	contents = r.text
	pattern = r'<a href="../(.+?)" title'
	results = re.search(pattern, contents)
	url3 = 'http://www.wsyyxz.com/e/DownSys/' + results.group(1)

	r = requests.get(url3, headers=HEADERS)
	baidu_url = r.url


def crawl_song(song_title):
	# search the given song by title
	payload = {'keyboard':song_name, 'tempid': 1, 'classid': u'1,2,3,4,5,6,7,8,9,10,11,12', 'show': u'title,newstext,ftitle', 'Submit22': u'搜索'}
	r = requests.post(search_url, data=payload, headers=HEADERS)
	contents = r.text

	# pattern = r'<li><a href="/song\?id=\d+">(.+?)</a></li>'
	pattern = r'<h2 class="r"><span>(\d+?)\.</span> <a class="l" href="(.+?)" target="_blank">(.+?)</a></h2>'
	song_list = re.findall(pattern, contents)
