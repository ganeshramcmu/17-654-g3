from flask import Flask, render_template, request, send_from_directory, jsonify
import sys
import optparse
import time
import random
import datetime
import global_config
import getLive
import machineLearning.train as train

modelA_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/PretrainedModel/modelA.joblib'
modelB_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/PretrainedModel/modelB.joblib'
Time_slots_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/Time_Slots.csv'

#list of all person ids used to train the model 
person_ids = [9351,5037,990,1688,3440,9419]

app = Flask(__name__, static_url_path='')
start = int(round(time.time()))

@app.route('/js/<path:path>')
def send_js_files(path):
    return send_from_directory('js', path)

@app.route("/internalDashboard")
def send_index_file():
	return render_template("index.html")

@app.route("/checkLivePredictionQuality")
def checkLivePredictionQuality():
	liveData = getLive.getLiveData()

	response = "Empty live Data"
	response_code = 404
	
	if liveData!="":
		liveDataList = liveData.split(";")
		mseData = liveDataList[0]
		cmuData = liveDataList[1]
		mseDataList = mseData.split(",")
		cmuDataList = cmuData.split(",")
		mseMorningDateTime=''
		mseEveningDateTime=''
		cmuMorningDateTime=''
		cmuEveningDateTime=''

		errorLive = "NA"
		response = "Error cannot be calculated because of malformed data"
		response_code = 404
		if mseDataList[0]!='none' and mseDataList[1]!='none' and cmuDataList[0]!='none' and cmuDataList[1]!='none' :
			errorLive = "A"
			#parse mseDataList
			mseMorningDateTime = mseDataList[0]
			mseEveningDateTime = mseDataList[1]

			#parse cmuDataList
			cmuMorningDateTime = cmuDataList[0]
			cmuEveningDateTime = cmuDataList[1]

		#mseMorningDateTime = "2018-10-10 10:12:12"
		#mseEveningDateTime = "2018-10-10 19:13:12"
		#cmuMorningDateTime = "2018-10-10 08:12:34"
		#cmuEveningDateTime = "2018-10-10 17:19:11"
		currentDateTime = datetime.datetime.now()
		currentDate = currentDateTime.strftime("%Y-%m-%d")
		
		#get prediction for "cmu" user
		person_index = random.randint(0,2)
		person_id = person_ids[person_index]
		#instance of modelA
		smartEnergyA = train.SmartEnergerA(modelA_path, Time_slots_path)
		predictionForModelA = smartEnergyA.predict(currentDate, person_id)

		#get prediction for "mse" user
		person_index = random.randint(3,5)
		person_id = person_ids[person_index]
		
		daytime = ""
		dayTimeHr = random.randint(8,14)
		dayTimeMin = random.randint(0,59)
		dayTimeSec = random.randint(0,59)
		daytime = str(dayTimeHr) +":"+ str(dayTimeMin) +":"+ str(dayTimeSec)

		#instance of modelB
		smartEnergyB = train.SmartEnergerB(modelB_path, Time_slots_path)
		predictionForModelB = smartEnergyB.predict(currentDate, person_id, daytime)

		response = "Prediction in model A or model B failed!"
		response_code = 503

		errorPred = "NA"
		if predictionForModelA == [] and predictionForModelB == []:
			errorPred = "NA"
			response = "Error cannot be calculated because of malformed data"
			response_code = 404
		elif predictionForModelA != [] and predictionForModelB != []:
			errorPred = "A"
			#parsing predictionForModelA
			light_on_minute_interval_A = predictionForModelA[0][-1]
			light_on_minute_A = predictionForModelA[0][-3:-1]
			light_on_hour_A = predictionForModelA[0][:-3]

			light_off_minute_interval_A = predictionForModelA[1][-1]
			light_off_minute_A = predictionForModelA[1][-3:-1]
			light_off_hour_A = predictionForModelA[1][:-3]

			#parsing predictionForModelB
			light_on_minute_interval_B = predictionForModelB[0][-1]
			light_on_minute_B = predictionForModelB[0][-3:-1]
			light_on_hour_B = predictionForModelB[0][:-3]

			light_off_minute_interval_B = predictionForModelB[1][-1]
			light_off_minute_B = predictionForModelB[1][-3:-1]
			light_off_hour_B = predictionForModelB[1][:-3]
			
			if errorLive == "NA":
				response = "Error cannot be calculated because of no live data"
				response_code=404
			if errorPred == "NA":
				response = "Error cannot be calculated because of prediction failure"
				response_code=503

			if errorLive != "NA" and errorPred != "NA":
				predictionMorningTimeA = currentDate + " " + light_on_hour_A + ":" + light_on_minute_A + ":00"
				predictionEveningTimeA = currentDate + " " + light_off_hour_A + ":" + light_off_minute_A + ":00"
				
				predictionMorningTimeB = currentDate + " " + light_on_hour_B + ":" + light_on_minute_B + ":00"
				predictionEveningTimeB = currentDate + " " + light_off_hour_B + ":" + light_off_minute_B + ":00"

				predictionMorningDateTimeA = datetime.datetime.strptime(predictionMorningTimeA, "%Y-%m-%d %H:%M:%S")
				predictionEveningDateTimeA = datetime.datetime.strptime(predictionEveningTimeA, "%Y-%m-%d %H:%M:%S")
				
				predictionMorningDateTimeB = datetime.datetime.strptime(predictionMorningTimeB, "%Y-%m-%d %H:%M:%S")
				predictionEveningDateTimeB = datetime.datetime.strptime(predictionEveningTimeB, "%Y-%m-%d %H:%M:%S")
				
				errorMorningA = (datetime.datetime.strptime(cmuMorningDateTime, "%Y-%m-%d %H:%M:%S") - predictionMorningDateTimeA).total_seconds()/60
				errorEveningA = (datetime.datetime.strptime(cmuEveningDateTime, "%Y-%m-%d %H:%M:%S") - predictionEveningDateTimeA).total_seconds()/60

				errorMorningB = (datetime.datetime.strptime(mseMorningDateTime, "%Y-%m-%d %H:%M:%S") - predictionMorningDateTimeB).total_seconds()/60
				errorEveningB = (datetime.datetime.strptime(mseEveningDateTime, "%Y-%m-%d %H:%M:%S") - predictionEveningDateTimeB).total_seconds()/60

				response_code=200
				response = {}
				response['errorMorningA'] = errorMorningA
				response['errorEveningA'] = errorEveningA
				response['errorMorningB'] = errorMorningB
				response['errorEveningB'] = errorEveningB
				response['predictionMorningTimeA'] = predictionMorningTimeA
				response['predictionEveningTimeA'] = predictionEveningTimeA
				response['predictionMorningTimeB'] = predictionMorningTimeB
				response['predictionEveningTimeB'] = predictionEveningTimeB
				response['mseMorningDateTime'] = mseMorningDateTime
				response['mseEveningDateTime'] = mseEveningDateTime
				response['cmuMorningDateTime'] = cmuMorningDateTime
				response['cmuEveningDateTime'] = cmuEveningDateTime

	responseObj = {}
	responseObj['response_code'] = response_code
	responseObj['data'] = response
	return jsonify(responseObj)


			

@app.route("/getModelPrediction")
def getModelPrediction():
	#username of the user using the system
	username = request.args.get("v")

	#result is a list that stores the model predictions
	result = []
	
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
		daytime = ""
		dayTimeHr = random.randint(8,14)
		dayTimeMin = random.randint(0,59)
		dayTimeSec = random.randint(0,59)
		daytime = str(dayTimeHr) +":"+ str(dayTimeMin) +":"+ str(dayTimeSec)

		person_index = random.randint(3,5)
		person_id = person_ids[person_index]
		#instance of modelA
		smartEnergyB = train.SmartEnergerB(modelB_path, Time_slots_path)
		result = smartEnergyB.predict(currentDate, person_id, daytime)

	response = "Prediction Failed"

	if result != []:
		light_on_minute_interval = result[0][-1]
		light_on_minute = result[0][-3:-1]
		light_on_hour = result[0][:-3]

		light_off_minute_interval = result[1][-1]
		light_off_minute = result[1][-3:-1]
		light_off_hour = result[1][:-3]
		
		light_on_time = "Predicted light on time in morning: " + light_on_hour + ":" + light_on_minute
		light_off_time = "Predicted light off time in evening: " + light_off_hour + ":" + light_off_minute
		response = light_on_time + "," + light_off_time
	
	return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=global_config.debug)