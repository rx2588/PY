# coding: utf-8

import json
import csv
import functools
import requests
from typing import List


def singleton(cls):
    __ins_map = {}
    
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in __ins_map:
            __ins_map[cls] = cls(*args, **kwargs)
        return __ins_map[cls]

    return wrapper



def load_json_from_file(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def load_json_field_from_file(path: str, field: str, default=None):
    return load_json_from_file(path).get(field, default)


def dump_str_to_file(s: str, output_path: str):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(s)


def dump_to_json(object: any, output_path: str):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(object, ensure_ascii=False, indent=4))


def dump_to_csv(data: List[dict], keys: List[str], output_path: str):
    simplify_data = []
    for item in data:
        simplify_data.append({k: item.get(k, '') for k in keys})

    with open(output_path, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(simplify_data)
    

def is_contains_words(s: str, words: List[str]) -> bool:
    for word in words:
        if s.find(word) != -1:
            return True
    return False


# tests

if __name__ == '__main__':
    data = [
        {
            'name': 'Peter',
            'age': 10,
            'gender': 'male'
        },
        {
            'name': 'Emma',
            'age': 16,
            'gender': 'female'
        }
    ]
    dump_to_csv(data, ['name', 'age', 'gender'], 'utils_dump_test.csv')
    