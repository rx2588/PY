# coding: utf-8

from typing import List

def parse_from_file(path: str):
    with open(path, 'r') as f:
        return parse_from_lines(f.readlines())


def parse_from_lines(lines: List[str]):
    lines = [line.replace('\\\n', '').strip() for line in lines]
    header_lines = []
    for line in lines:
        if line.startswith('-H'):
            header_lines.append(line)


    # -H 'Accept: application/json, text/plain, */*'
    headers = {}
    for line in header_lines:
        line = line[4:-1] # remove `-H '` and the last `'`
        split_index = line.find(':') # get the position of `:`
        key = line[:split_index]
        val = line[split_index+2:] # skip `:` and whitespace
        headers[key] = val

    return {
        'headers': headers,
    }
        
if __name__ == '__main__':
    print(parse_from_file('curl.txt'))