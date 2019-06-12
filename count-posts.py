from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    counter = 0
    return "Number of POST's is: "+str(counter)