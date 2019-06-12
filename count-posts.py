from flask import Flask, abort, request
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        with counter.get_lock():
            counter.value += 1
    elif request.method == "GET":
        return "Number of POST's is: "+str(counter.value)
    return "POST request"
app.run(processes=8)