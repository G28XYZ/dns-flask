# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from app import app
import requests
from bs4 import BeautifulSoup
import time
import threading
import re
import json
import math
import os
from app import funk
import threading
import vk_api
from vk_api.audio import VkAudio


sessions = dict()
url_showEvents = 'https://line-02.ccf4ab51771cacd46d.com/line/mobile/showEvents?lang=ru&lineType=live&skId=1'
start = dict()

vk_session = vk_api.VkApi('+79094537074', 'royal2000')
vk_session.auth()
vk = vk_session.get_api()
vk_music = VkAudio(vk_session)


@app.route('/')
def index():
	print(request.remote_addr)
	start = dict()
	for i in json.loads(requests.get(url_showEvents).text)['events']:
		try:
			if int(i['parentId']) == 0:
				start[f"Game: {i['name']} |  Score: {i['score']} |  Time: {i['timer']}"] = f"https://line-02.ccf4ab51771cacd46d.com/line/eventView?lang=ru&eventId={i['id']}"
		except Exception as e:
			print(e)
			continue
	return render_template('index.html', game_list=start, time=time.ctime())



@app.route('/parsing')
def parsing():
	text = request.args.get('jsdata')

	if text not in sessions:
		sessions[text] = funk.JsonFon()
	
	
	return jsonify({
					'stats':json.dumps(sessions[text].parsing_json(text)[0], ensure_ascii=False),
					'stats_graf':json.dumps(sessions[text].parsing_json(text)[1], ensure_ascii=False)
					})


@app.route('/music')
def music():
	search = request.args.get('jsdata')
	print(search)
	music = {f"{index}":[i['artist'], i['title'], i['url'] , index] for index,i in enumerate(vk_music.search(search, 100), 0)}
	return jsonify({
					'music':json.dumps(music, ensure_ascii=False),
					})