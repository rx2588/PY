# coding: utf-8

import random
import time
import requests
from loguru import logger
from pkg import utils

template_url = 'https://cuttlefish.baidu.com/user/interface/getquerypacklist?cid={cid}&pn={page}&rn=20&word=&tab=1'
# cid: 类别 id，0: 学前教育 ，1: 基础教育，高校与高等教育，语言/资格考试，法律，建筑，互联网，行业资料，政务民生，商品说明书，实用模版，生活娱乐
# pn: 页数，从 0 开始，最多 10 页（即最大为 9）
cid_map = {
    0: '学前教育',
    1: '基础教育',
    2: '高校与高等教育',
    3: '语言/资格考试',
    4: '法律',
    5: '建筑',
    6: '互联网',
    7: '行业资料',
    8: '政务民生',
    9: '商品说明书',
    10: '实用模版',
    11: '生活娱乐',
    99: '推荐',
}
page_list = list(range(10))


def fetch_tasks(cid: int, page: int, headers: dict):
    url = template_url.format(cid=cid, page=page)
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(
            f'unexpected http response status code: {resp.status_code} resp.content: {resp.content}')

    resp_json = resp.json()

    if resp_json['status']['code'] != 0:
        code, msg = resp_json['status']['code'], resp_json['status']['msg']
        logger.warning(f'unexpected response status code, code={code}, msg={msg}')
        return None

    query_list = resp_json['data']['queryList']
    tasks = []
    for item in query_list:
        if item['status'] != 1:
            # 状态异常：已经完成或者其他
            continue
        tasks.append({
            'cid': cid,
            'category': cid_map[cid],
            'title': item['queryName'],
            'page': page,
            'estimated_price': item['estimatedPrice'],
            'status': item['status'],
        })

    return tasks


def fetch_tasks_of_cid(headers: dict, cid: int):
    tasks = []
    page = 0

    while True:
        logger.info(f'fetching tasks, cid={cid} page={page}, already fetched {len(tasks)} tasks')
        page_tasks = fetch_tasks(cid, page, headers)        
        if page_tasks is None:
            break

        logger.info(f'tasks fetched, cid={cid}, page={page}, number of tasks={len(page_tasks)}')
        tasks.extend(page_tasks)
        time.sleep(random.randint(200, 500) / 100.0) # sleep 200 ~ 500 ms
        page += 1
            
    return tasks


def fetch_all_tasks(headers: dict):
    tasks = []

    settings = utils.load_json_from_file('conf/settings.json')
    cid_list = settings['fetch_tasks']['categories']

    for cid in cid_list:
        cid_tasks = fetch_tasks_of_cid(headers, cid)
        tasks.extend(cid_tasks)
        time.sleep(random.randint(200, 500) / 100.0) # sleep 200 ~ 500 ms
            
    return tasks
