import json

def open_counter_json():
    with open('counter.json', 'r') as file:
        json_data = json.load(file)
    return json_data

def read_counter_from_json(json_data):
    return json_data['Counter']

def write_counter_to_json(json_data, counter):
    json_data['Counter'] = counter
    with open('counter.json', 'w') as file:
        json.dump(json_data, file)
    return