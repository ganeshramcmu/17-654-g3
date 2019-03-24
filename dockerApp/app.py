from flask import Flask, render_template, request, send_from_directory
import sys
import optparse
import time
import train

app = Flask(__name__, static_url_path='')
start = int(round(time.time()))

@app.route('/js/<path:path>')
def send_js_files(path):
    return send_from_directory('js', path)

@app.route("/internalDashboard")
def send_index_file():
	print(request.args.get('x'))
	return render_template("index.html")

@app.route("/getModelPrediction?v=?")
def getModelAPrediction():
	print("Model A prediction")
	result = train.SmartEnergerA.predict("some date", 1, 2)
	return result

@app.route("/getModelBPrediction")
def getModelBPrediction():
	print("Model B prediction")
	result = train.SmartEnergerB.predict("some date", 1,2,3)
	return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)