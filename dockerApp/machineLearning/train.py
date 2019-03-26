from joblib import dump, load
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


'''
This is will be the first machine learning model, that only use date, 
hours and minutes, people id as the training attributes. This will be 
our baseline model. 
'''

class SmartEnergerA():

	classifier = None
	time_slots_path = None

	# model_path is the path for the pretrained model in the system. 
	# time_slots path is the path for the Time_slots.csv file. 
	def __init__(self, model_path, Time_slots_path):
		self.classifier = load(model_path) 
		self.time_slots_path = Time_slots_path

	# date should have the format year-month-day.
	# pid should be one of the six people id strings.
	# sunsetTime should have the format hour:minute:sec
	def predict(self, date, pid):
		x = self.xGenerator(date, pid)
		prediction = self.classifier.predict(x)
		for i in prediction:
			print(i)

		# 4:00 - 16:00 is morning time, we find the first 1.
		light_on_time_check = prediction[0:1441]

		# 16:01 - 3:39 is evening time, we find the last 1. 
		light_off_time_check = prediction[1441:]
		
		light_on_time_index = 1440
		for i in range(len(light_on_time_check)):
			if light_on_time_check[i] == 1:
				light_on_time_index = i
				break
			i += 1

		light_off_time_index = 0
		j = len(light_off_time_check) - 1
		while (j > 0):
			if light_off_time_check[j] == 1:
				light_off_time_index = i
				break
			j -= 1
		light_off_time_index += 1440

		light_on_time = self.findTime(light_on_time_index)
		light_off_time = self.findTime(light_off_time_index)

		return light_on_time, light_off_time

	def findTime(self, index):
		with open(self.time_slots_path, 'r') as f:
			data = f.readlines()
		f.close()
		return data[index].strip('\n')

	def xGenerator(self, date, pid):

		with open(self.time_slots_path, 'r') as f:
			data = f.readlines()
		f.close()

		result = []
		for i in data:
			i = i.strip('\n')
			content = []
			content.append(int(date))
			content.append(int(i))
			content.append(int(pid))
			result.append(content)		
		return result
		
'''
This is the second machine learning model, a more advanced one compared with 
SmartEnergerA. It makes the predictions based on on more attributes, which is 
the sunset time for that day in Pittsburgh.
'''
class SmartEnergerB():

	classifier = None
	time_slots_path = None

	# model_path is the path for the pretrained model in the system. 
	# time_slots path is the path for the Time_slots.csv file. 
	def __init__(self, model_path, Time_slots_path):
		self.classifier = load(model_path) 
		self.time_slots_path = Time_slots_path

# date should have the format year-month-day.
	# pid should be one of the six people id strings.
	# sunsetTime should have the format hour:minute:sec
	# daytime is the day length for date day. 
	# should have the format hh:mm:ss
	def predict(self, date, pid, daytime):
		x = self.xGenerator(date, pid, daytime)
		prediction = self.classifier.predict(x)

		# 4:00 - 16:00 is morning time, we find the first 1.
		light_on_time_check = prediction[0:1441]

		# 16:01 - 3:39 is evening time, we find the last 1. 
		light_off_time_check = prediction[1441:]
		
		light_on_time_index = 1440
		for i in range(len(light_on_time_check)):
			if light_on_time_check[i] == 1:
				light_on_time_index = i
				break
			i += 1

		light_off_time_index = 0
		j = len(light_off_time_check) - 1
		while (j > 0):
			if light_off_time_check[j] == 1:
				light_off_time_index = i
				break
			j -= 1
		light_off_time_index += 1440

		light_on_time = self.findTime(light_on_time_index)
		light_off_time = self.findTime(light_off_time_index)

		return light_on_time, light_off_time

	def findTime(self, index):
		with open(self.time_slots_path, 'r') as f:
			data = f.readlines()
		f.close()
		return data[index].strip('\n')

	def xGenerator(self, date, pid, daytime):

		with open(self.time_slots_path, 'r') as f:
			data = f.readlines()
		f.close()

		h, m, s = daytime.split(':')
		daytime = h + m + s
		result = []
		for i in data:
			i = i.strip('\n')
			content = []
			content.append(int(date))
			content.append(int(daytime))
			content.append(int(i))
			content.append(int(pid))
			result.append(content)		
		return result