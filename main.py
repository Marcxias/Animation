# -*- coding: utf-8 -*-

import os
import json

import arrow
import requests

from bs4 import BeautifulSoup


def getPage(year):
	"""Fetch corresponding page.
	"""

	# Url
	requestUrl = f'https://zh.wikipedia.org/zh-cn/日本動畫列表_({year}年)'

	return requests.get(requestUrl).text


def tableDict(page):
	"""Generate a single table.
	"""

	soup = BeautifulSoup(page, 'html.parser')

	tables = soup.find_all('table')

	return {
		'spring': tables[0],
		'summer': tables[1],
		'autumn': tables[2],
		'winter': tables[3],
		'ova': tables[4],
		'film': tables[5]
	}


def extract(table, type):
	"""Generate a single row.
	"""

	preList1 = filter(lambda x: x != '\n', table.contents)

	preList2 = [i for i in filter(lambda x: x != '\n', preList1)]

	preList3 = [list(filter(lambda x: x != '\n', t)) for t in [i.contents for i in preList2]][1:]

	return list(filter(lambda x: len(x) == 5, map(lambda x: dict(zip(
			getKeyList(type), 
			[i.text.strip() for i in x]
		)), preList3)))


def getKeyList(type):
	"""Get corresponding key list.
	"""
	if type in ('spring', 'summer', 'autumn', 'winter'):
		return ['开始日－结束日', '作品名', '原名', '制作公司', '话数']
	else:
		return {
			'film': ['上映日', '作品名', '原名', '制作公司', '备注'],
			'ova': ['发售日期', '作品名', '原名', '制作公司', '备注']
		}[type]


def serlize(year, type):
	"""A simple wrapper for all funcs.
	"""

	page = getPage(year)
	table = tableDict(page)[type]
	content = extract(table, type)

	return content


if __name__ == '__main__':

	typeMatrix = [
		'spring',
		'summer',
		'autumn',
		'winter',
		'film',
		'ova'
	]

	# Get this year
	thisYear = arrow.utcnow().to('Asia/Shanghai').year

	yearMatrix = list(range(2009, thisYear + 1))

	os.mkdir('Resources')

	for y in yearMatrix:
		os.mkdir(f'Resources/{y} 年')
		for t in typeMatrix:
			with open(f'Resources/{y} 年/{y} {t.title()}.json', 'w') as f:
				json.dump(serlize(y, t), f, indent=4, ensure_ascii=False)

