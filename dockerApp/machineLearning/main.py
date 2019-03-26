from train import SmartEnergerA, SmartEnergerB


# data = all_day('20180918', '990', '/home/hotel/machineLearning/Time_Slots.csv')
# print(data)

modelA_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/PretrainedModel/modelA.joblib'
modelB_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/PretrainedModel/modelB.joblib'
Time_slots_path = '/Users/ganeshramks/Downloads/AnalysisOfSoftwareArtifacts/assignments/group_assignment_3/17-654-g3/dockerApp/machineLearning/Time_Slots.csv'

# test = SmartEnergerB(modelB_path, Time_slots_path)
# a = test.predict('20180908', '990', '05:20:56')

test = SmartEnergerA(modelA_path, Time_slots_path)
a = test.predict('20180908', '8860000')

for i in a:
	print(i)