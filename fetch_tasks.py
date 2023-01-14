# coding: utf-8

from pkg.parse_curl import parse_from_file
from pkg import task_spider
from pkg import utils

def main():
    curl_data = parse_from_file('conf/fetch_tasks_curl.txt')
    headers = curl_data['headers']

    # dump to json for debug
    # utils.dump_to_json(headers, 'headers.json')

    tasks = task_spider.fetch_all_tasks(headers)
    task_fields = ['title', 'cid', 'category', 'page', 'estimated_price', 'status']
    utils.dump_to_csv(tasks, task_fields, 'output/tasks.csv')


if __name__ == '__main__':
    main()
