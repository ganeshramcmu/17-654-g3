from flask import Flask, render_template, request, send_from_directory
import sys
import optparse
import time
import random
import datetime
import global_config
import machineLearning.train as train

app = Flask(__name__, static_url_path='')
start = int(round(time.time()))

@app.route('/js/<path:path>')
def send_js_files(path):
    return send_from_directory('js', path)

@app.route("/internalDashboard")
def send_index_file():
	print(request.args.get('x'))
	return render_template("index.html")

@app.route("/getModelPrediction")
def getModelPrediction():
	print("Model prediction")
	#username of the user using the system
	username = request.args.get("x")
	#result is a list that stores the model predictions
	result = []
	#list of all person ids used to train the model 
	person_ids = [9351,5037,990,1688,3440,9419]
	
	currentDateTime = datetime.datetime.now()
	currentDate = currentDateTime.strftime("%Y-%m-%d")
	
	#Model A will be used for user cmu
	if username=="cmu":
		person_index = random.randint(0,2)
		person_id = person_ids[person_index]

		#result = train.SmartEnergerA.predict("dummy", "2019-03-25", person_id)
		result="Predicted morning close time: 09:00 AM,Predicted evening open time: 10:00 PM"
	#Model B will be used for user mse
	elif username=="mse":
		person_index = random.randint(3,5)
		person_id = person_ids[person_index]

		result = train.SmartEnergerB.predict("dummy", currentDate, person_id)
	
	return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=global_config.debug)