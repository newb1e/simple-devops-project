from flask import Flask, abort, request
from multiprocessing import Value
import json
from Counter import counter

# Read Counter value from Json. 
# This way previouse count will be included.
counter_from_json = counter.read_counter_from_json(counter.open_counter_json())
# Used multiprocessing.Value. This synchronizes access to a 
# shared value across processes, as long as the processes 
# are spawned after the value is created.
counter_value = Value('i', counter_from_json)
app = Flask(__name__)

# counter_service function will check if the http method
# is POST/GET. If GET, return number of POST requests.
# Else, if http method is POST, update number of POST
# requests at the json file.
@app.route('/', methods=['GET', 'POST'])
def counter_service():
    if request.method == "POST":
        with counter_value.get_lock():
            counter_value.value += 1
            counter.write_counter_to_json(counter.open_counter_json(),counter_value.value)
    elif request.method == "GET":
        return "Number of POST's is: "+str(counter_value.value)
    return "POST request"

app.run(processes=8)