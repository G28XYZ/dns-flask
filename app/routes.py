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

sessions = dict()

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/parsing')
def parsing():
	text = request.args.get('jsdata')

	if text not in sessions:
		sessions[text] = funk.JsonFon()
	
	return jsonify({
			'stats':json.dumps(sessions[text].parsing_json(text)[0], ensure_ascii=False),
			'stats_graf':json.dumps(sessions[text].parsing_json(text)[1], ensure_ascii=False)
			})

