import json

def load_json(fileName):
    return json.load(open(fileName, encoding='utf-8'))

