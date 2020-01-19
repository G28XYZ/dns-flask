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
import psycopg2

sessions = dict()
url_showEvents = 'https://line-02.ccf4ab51771cacd46d.com/line/mobile/showEvents?lang=ru&lineType=live&skId=1'

vk_number = os.environ.get('VK_NUMBER')
vk_password = os.environ.get('VK_PASSWORD')
vk_session = vk_api.VkApi(str(vk_number), vk_password)
vk_session.auth()
vk = vk_session.get_api()
vk_music = VkAudio(vk_session)

dbPath = str(os.environ.get('DATABASE_URL'))
db_HOST = str(os.environ.get('HOST'))
db_DATABASE = str(os.environ.get('DATABASE'))
db_USER = str(os.environ.get('USER'))
db_PASSWORD = str(os.environ.get('PASSWORD'))

def db_commit():
    conn = psycopg2.connect(database = db_DATABASE,
                            user = db_USER,
                            password = db_PASSWORD,
                            host = db_HOST,
                            port = "5432")
    cur = conn.cursor()
    try:
        cur.execute("SELECT _ip_ from DB_IP_test")
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute(f"INSERT INTO DB_IP_test (_IP_, FIRST_VISIT, LAST_VISIT) VALUES ('{request.remote_addr}', '{time.ctime()}', '{time.ctime()}')")
            conn.commit()
        if str(request.remote_addr) not in [''.join(*list(i)) for i in rows]:
            cur.execute(f"INSERT INTO DB_IP_test (_IP_, FIRST_VISIT, LAST_VISIT) VALUES ('{request.remote_addr}', '{time.ctime()}', '{time.ctime()}')")
            conn.commit()
        else:
            cur.execute(f"UPDATE DB_IP_test set LAST_VISIT = '{time.ctime()}' where _IP_ = '{request.remote_addr}'")
            conn.commit()
    except Exception as e:
        print(e)
    conn.close()

@app.route('/')
def index():
	try:
		db_commit()
		start = {i['name']:f"https://line-02.ccf4ab51771cacd46d.com/line/eventView?lang=ru&eventId={i['id']}" for i in json.loads(requests.get(url_showEvents).text)['events'] if int(i['parentId']) == 0}
	except Exception as e:
		print(e)
	return render_template('index.html', game_list=start)


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
