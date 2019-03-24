from flask import Flask, render_template, request
import sys
import optparse
import time

app = Flask(__name__)
start = int(round(time.time()))

@app.route("/")
def send_index_file():
	return render_template("index.html")

@app.route("getModelAPrediction")
def getModelAPrediction():
	

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)