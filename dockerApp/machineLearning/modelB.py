from sklearn.neural_network import MLPClassifier
from joblib import dump, load
import numpy as np
from sklearn.linear_model import SGDClassifier

train_x = np.load('dataB/trainB_x.npy')
train_y = np.load('dataB/trainB_y.npy')

vali_x = np.load('dataB/valiB_x.npy')
vali_y = np.load('dataB/valiB_y.npy')

train_x = train_x.tolist()
train_y = train_y.tolist()

print(vali_x.shape)
print(vali_y.shape)

vali_x = vali_x.tolist()
vali_y = vali_y.tolist()

# mlp = MLPClassifier(hidden_layer_sizes=(10, 20, 30, 20, 10), max_iter=150, alpha=1e-4,
#                     solver='adam', verbose=10, tol=1e-4, random_state=1,
#                     learning_rate_init=0.1, shuffle=True)

# classifier = MLPClassifier(solver='lbfgs', alpha=1e-5,
# 	hidden_layer_sizes=(30, 30), random_state=1, verbose=True)
# mlp.fit(train_x, train_y)

# score = mlp.score(vali_x, vali_y)
# print(score)


clf = SGDClassifier(loss="log", penalty="l2", max_iter=150, 
	tol=1e-4, shuffle=True, verbose=1)
clf.fit(train_x, train_y) 
score = clf.score(vali_x, vali_y)
print(score)



# with open('data_B.csv', 'r') as f:
# 	data = f.readlines()

# f.close()

# raw_data = []

# for i in data:
# 	i = i.strip('\n')
# 	date, daylength, time, pid, label = i.split(',')
# 	temp_x = []
# 	temp_y = []

# 	temp_x.append(date)
# 	temp_x.append(daylength)
# 	temp_x.append(time)
# 	temp_x.append(pid)

# 	temp_data = []
# 	temp_x = np.asarray(temp_x, dtype=np.intc)

# 	temp_data.append(temp_x)
# 	temp_data.append(int(label))
# 	temp_data = np.asarray(temp_data)

# 	raw_data.append(temp_data)
# 	# raw_data.append(temp_x)
# 	# raw_data.append(temp_y)

# # x = np.asarray(x)
# raw_data = np.asarray(raw_data)
# # print(raw_data.shape)
# # print(raw_data[0].shape)
# # print(raw_data[0][0])
# # print(raw_data[0][1])
# np.save('raw_data_B.npy', raw_data)