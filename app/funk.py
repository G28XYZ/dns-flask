import requests
import math
import json

param_list_1 = ["1-й тайм угловые",
                "1-й тайм желтые карты",
                "1-й тайм фолы",
                "1-й тайм удары в створ",
                "1-й тайм офсайды",
                "1-й тайм вброс аутов",
                "1-й тайм удары от ворот"]


param_list_2 = ["угловые",
                "желтые карты",
                "фолы",
                "удары в створ",
                "офсайды",
                "вброс аутов",
                "удары от ворот"]


class JsonFon():
	def __init__(self):
		self.T = 0
		self.url = ''
		self.stats = dict()
		self.dict_graf = dict()

	def parsing_json(self, url):
		self.url = url

		json_match_info = json.loads(requests.get(self.url).text)

		self.stats['timer'] = json_match_info['events'][0]['timer']
		self.stats['team1'] = json_match_info['events'][0]['team1']
		self.stats['team2'] = json_match_info['events'][0]['team2']
		self.stats['score'] = json_match_info['events'][0]['score']
		self.stats['game'] = f"{self.stats['team1']}   {self.stats['score']}   {self.stats['team2']}"

		try:
			self.stats['scoreComment'] = json_match_info['events'][0]['scoreComment']
		except Exception as e:
			print(e)

		if '1-й тайм' in str(json_match_info['events']):
			self.T = 1
			self.stats["TIME"] = self.T
		else:
			self.T = 0
			self.stats["TIME"] = self.T

		for i in range(len(json_match_info['events'])):
			if self.T:
				name_param = json_match_info['events'][i]['name']
				if name_param in param_list_1:
					score = json_match_info['events'][i]['score']
					tb = json_match_info['events'][i]['subcategories'][0]['quotes'][0]['p']
					tb_value = json_match_info['events'][i]['subcategories'][0]['quotes'][0]['value']
					tm = json_match_info['events'][i]['subcategories'][0]['quotes'][1]['p']
					tm_value = json_match_info['events'][i]['subcategories'][0]['quotes'][1]['value']

					try:

						k1 = int(score.split('-')[0])
						k2 = int(score.split('-')[1])
						t = int(tb.split('.')[0])
						self.stats[f"{name_param.replace('1-й тайм ', '')} K1"] = str(k1)
						self.stats[f"{name_param.replace('1-й тайм ', '')} K2"] = str(k2)
						self.stats[f"{name_param.replace('1-й тайм ', '')} Total"] = f"Total - {tb}"
						self.stats[f"{name_param.replace('1-й тайм ', '')} БМ"] = f"Б-{tb_value} | М-{tm_value}"
						self.stats[f"{name_param.replace('1-й тайм ', '')}"] = t - (k1+k2)

						time_min = int(self.stats['timer'].split(':')[0])

						if '{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min) not in self.dict_graf:
							if '{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min - 1) in self.dict_graf:
								until_k1 = self.dict_graf['{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min-1)][0]
								until_k2 = self.dict_graf['{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min-1)][1]
								self.dict_graf['{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min)] = [k1, k2, t, (k1+k2) - (until_k1 + until_k2)]
							else:
								self.dict_graf['{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min)] = [k1, k2, t, 0]
					
					except Exception as e:
						print(e)
						

			else:
				name_param = json_match_info['events'][i]['name']
				if name_param in param_list_2:
					score = json_match_info['events'][i]['score']
					tb = json_match_info['events'][i]['subcategories'][0]['quotes'][0]['p']
					tm = json_match_info['events'][i]['subcategories'][0]['quotes'][1]['p']
					tb_value = json_match_info['events'][i]['subcategories'][0]['quotes'][0]['value']
					tm_value = json_match_info['events'][i]['subcategories'][0]['quotes'][1]['value']

					try:

						k1 = int(score.split('-')[0])
						k2 = int(score.split('-')[1])
						t = int(tb.split('.')[0])
						self.stats[f"{name_param.replace('1-й тайм ', '')} K1"] = str(k1)
						self.stats[f"{name_param.replace('1-й тайм ', '')} K2"] = str(k2)
						self.stats[f"{name_param.replace('1-й тайм ', '')} Total"] = f"Total - {tb}"
						self.stats[f"{name_param.replace('1-й тайм ', '')} БМ"] = f"Б-{tb_value} | М-{tm_value}"
						self.stats[f"{name_param.replace('1-й тайм ', '')}"] = t - (k1+k2)

						time_min = int(self.stats['timer'].split(':')[0])

						if '{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min) not in self.dict_graf:
							if '{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min - 1) in self.dict_graf:
								until_k1 = self.dict_graf['{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min-1)][0]
								until_k2 = self.dict_graf['{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min-1)][1]
								self.dict_graf['{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min)] = [k1, k2, t, (k1+k2) - (until_k1 + until_k2)]
							else:
								self.dict_graf['{} - {} минута'.format(name_param.replace('1-й тайм ', ''), time_min)] = [k1, k2, t, 0]
					
					except Exception as e:
						print(e)


		return [self.stats, self.dict_graf]
