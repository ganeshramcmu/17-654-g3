from flask import Flask, render_template, request, send_from_directory
import sys
import optparse
import time
import random
import datetime
import global_config
import machineLearning.train as train

modelA_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/PretrainedModel/modelA.joblib'
modelB_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/PretrainedModel/modelB.joblib'
Time_slots_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/Time_Slots.csv'

app = Flask(__name__, static_url_path='')
start = int(round(time.time()))

@app.route('/js/<path:path>')
def send_js_files(path):
    return send_from_directory('js', path)

@app.route("/internalDashboard")
def send_index_file():
	return render_template("index.html")

@app.route("/getModelPrediction")
def getModelPrediction():
	print("Model prediction")
	#username of the user using the system
	username = request.args.get("v")

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
		#instance of modelA
		smartEnergyA = train.SmartEnergerA(modelA_path, Time_slots_path)
		result = smartEnergyA.predict(currentDate, person_id)
		
	#Model B will be used for user mse
	elif username=="mse":
		person_index = random.randint(3,5)
		person_id = person_ids[person_index]
		#instance of modelA
		smartEnergyB = train.SmartEnergerB(modelB_path, Time_slots_path)
		result = smartEnergyB.predict(currentDate, person_id)

	response = "Prediction Failed"

	if result != []:
		light_on_minute_interval = result[0][-1]
		light_on_minute = result[0][-3:-1]
		light_on_hour = result[0][:-3]

		light_off_minute_interval = result[1][-1]
		light_off_minute = result[1][-3:-1]
		light_off_hour = result[1][:-3]
		
		response = "Predicted light on time in morning: " + light_on_hour + ":" + light_on_minute + "," + "Predicted light off time in evening: " + light_off_hour + ":" + light_off_minute
	
	return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=global_config.debug)