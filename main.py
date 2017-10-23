# -*- coding: utf-8 -*-

import os
import json
from concurrent.futures import ProcessPoolExecutor

import arrow
import requests
from bs4 import BeautifulSoup


def getPage(year):
    """Fetch corresponding page.
    """

    requestUrl = f'https://zh.wikipedia.org/zh-cn/日本動畫列表_({year}年)'

    return requests.get(requestUrl).text


def tableDict(page):
    """Generate a single table.
    """

    soup = BeautifulSoup(page, 'html.parser')

    tables = soup.find_all('table')

    return dict(zip([
        'spring', 'summer', 'autumn', 'winter', 'ova', 'film'
        ], tables))


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

    thisYear = arrow.utcnow().to('Asia/Shanghai').year

    yearMatrix = range(2009, thisYear + 1)

    os.mkdir('Resources')

    list(map(os.mkdir, [f'Resources/{y} 年' for y in yearMatrix]))

    def marshal(info):
        y, t = info
        with open(f'Resources/{y} 年/{y} {t.title()}.json', 'w') as f:
            json.dump(serlize(y, t), f, indent=4, ensure_ascii=False)
        return f'{y} {t.title()} finished.'

    with ProcessPoolExecutor(max_workers=4) as executor:
        for i in executor.map(marshal, [(y, t) for y in yearMatrix for t in typeMatrix]):
            print(i)
    