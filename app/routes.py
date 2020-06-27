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
import traceback

url_showEvents = 'https://line41.bkfon-resource.ru/line/mobile/showEvents?lang=ru&lineType=live&skId=1&scopeMarket=1600'

_boolean_ = 0
json_dict = dict()
json_dict["url"] = url_showEvents
json_dict["ids"] = dict()

sessions = dict()

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
				start[f"Game: {i['name']} |  Score: {i['score']} |  Time: {i['timer']}"] = f"https://line13.bkfon-resource.ru/line/eventView?lang=ru&eventId={i['id']}&scopeMarket=1600"
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
				      

				      
def run_loop_thread():
	global json_dict
	while True:
		time.sleep(1)
		url_events = 'https://line41.bkfon-resource.ru/line/mobile/showEvents?lang=ru&lineType=live&skId=1&scopeMarket=1600'

		html = json.loads(requests.get(url_events).text)

		_list_1 = ["1-й тайм угловые",
				"1-й тайм фолы",
				"1-й тайм удары в створ",
				"1-й тайм вброс аутов",
				"1-й тайм удары от ворот"]


		_list_2 = ["угловые",
				"фолы",
				"удары в створ",
				"вброс аутов",
				"удары от ворот"]

		main_id = ""

		for index in html["events"]:

			name_team = f"{index['team1']} {index['team2']}"

			if index["parentId"] == 0:
				main_id = index["id"]

				try:
					if main_id in json_dict["ids"] and int(index["timer"].split(":")[0]) > 79:
						del json_dict["ids"][main_id]
						continue
				except:
					print()

				if main_id not in json_dict["ids"]:
					timer = ""
					try:
						timer = index["timer"]
					except Exception as e:
						print(f"\n\n\n>>>{e}<<<\n\n\n {traceback.format_exc()}")
						continue

					if timer != "":
						if int(timer.split(":")[0]) <= 5 or int(timer.split(":")[0]) == 45:
							json_dict["ids"][main_id] = dict()
							json_dict["ids"][main_id]["name_team"] = name_team
							json_dict["ids"][main_id]["timer"] = timer

				if main_id in json_dict["ids"]:
					if int( index["timer"].split(":")[0] ) <= 5 or int( index["timer"].split(":")[0] ) == 45:
						json_dict["ids"][main_id]["timer"] = index["timer"]

			try:
				if name_team == json_dict["ids"][main_id]["name_team"]:
					if int(json_dict["ids"][main_id]["timer"].split(":")[0]) <= 5:
						if index["name"] in _list_1:
							name_param = index["name"].replace("1-й тайм ", "")
							if name_param not in json_dict["ids"][main_id]:
								for sub in index["subcategories"]:
									if sub["name"] == "Тотал":
										json_dict["ids"][main_id][name_param] = float(sub["quotes"][0]["p"]) - ( int(index["score"].split("-")[0]) + int(index["score"].split("-")[1])) + ( 0.5 if sub["quotes"][1]["value"] >= 1.85 else 0)

					if int(json_dict["ids"][main_id]["timer"].split(":")[0]) == 45:
						if index["name"] in _list_2:
							name_param = index["name"]
							if name_param not in json_dict["ids"][main_id]:
								for sub in index["subcategories"]:
									if sub["name"] == "Тотал":
										json_dict["ids"][main_id][name_param] = float(sub["quotes"][0]["p"]) - ( int(index["score"].split("-")[0]) + int(index["score"].split("-")[1])) + ( 0.5 if sub["quotes"][1]["value"] >= 1.85 else 0)

						if name_param in json_dict["ids"][main_id]:
							if int(json_dict["ids"][main_id]["timer"].split(":")[0]) == 45:
								for sub in index["subcategories"]:
									if sub["name"] == "Тотал":
										json_dict["ids"][main_id][name_param] = float(sub["quotes"][0]["p"]) - ( int(index["score"].split("-")[0]) + int(index["score"].split("-")[1])) + ( 0.5 if sub["quotes"][1]["value"] >= 1.85 else 0)
			except Exception as e:
				print(f"\n\n\n>>>{e}<<<\n\n\n {traceback.format_exc()}")

thread_loop = threading.Thread(target=run_loop_thread)
            
@app.route('/total_on_time', methods = ['POST', 'GET'])
def total_on_time():
	global json_dict, _boolean_
	if _boolean_ == 0:
		_boolean_ = 1
		print("\n\nRUN_LOOP\n\n")
		thread_loop.start()
					  
	return render_template( 'index_for_total.html', json_dict=json.dumps(json_dict, ensure_ascii=False) )
#     return Response(stream_with_context(next(generated_page())))
