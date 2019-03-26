from sklearn.neural_network import MLPClassifier
from joblib import dump, load
import numpy as np
from sklearn.linear_model import SGDClassifier

train_x = np.load('dataA/trainA_x.npy')
train_y = np.load('dataA/trainA_y.npy')


vali_x = np.load('dataA/valiA_x.npy')
vali_y = np.load('dataA/valiA_y.npy')

train_x = train_x.tolist()
train_y = train_y.tolist()

print(vali_x.shape)
print(vali_y.shape)

vali_x = vali_x.tolist()
vali_y = vali_y.tolist()


# clf = SGDClassifier(loss="log", penalty="l2", max_iter=150, 
# 	tol=1e-4, shuffle=True, verbose=1)
# clf.fit(train_x, train_y) 
# score = clf.score(vali_x, vali_y)
# print(score)

mlp = MLPClassifier(hidden_layer_sizes=(10, 20, 30), max_iter=150, alpha=1e-4,
                    solver='adam', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=0.1, shuffle=True)

# classifier = MLPClassifier(solver='lbfgs', alpha=1e-5,
# 	hidden_layer_sizes=(30, 30), random_state=1, verbose=True)
mlp.fit(train_x, train_y)

score = mlp.score(vali_x, vali_y)
print(score)

# dump(mlp, 'modelA.joblib') 





# print(train_x)



# new_train_y = np.asarray(new_train_y)
# np.save('train_y.npy', new_train_y)




# train_data = np.load('test_data.npy')

# train_x = []
# train_y = []

# for i in train_data:
# 	train_x.append(i[0])
# 	train_y.append(i[1])
# 	# print(i[0])
# 	# print(i[1])

# train_x = np.asarray(train_x)
# train_y = np.asarray(train_y)

# print(train_x.shape)
# print(train_y.shape)

# np.save('test_x.npy', train_x)
# np.save('test_y.npy', train_y)


# print(train_data.shape)

# data = np.load('raw_data.npy')
# np.random.shuffle(data)
# # train_len = len(data) * 0.9
# # print(train_len)
# train_len = 2335589
# test_len = 25951


# train_data = data[:train_len]
# vali_data = data[train_len:]
# test_data = vali_data[:test_len]
# vali_data = vali_data[test_len:]
# print(len(train_data))
# print(len(vali_data))
# print(len(test_data))

# np.save('train_data.npy', train_data)
# np.save('vali_data.npy', vali_data)
# np.save('test_data.npy', test_data)

# train



# with open('data_7.csv', 'r') as f:
# 	data = f.readlines()
# f.close()

# raw_data = []

# for i in data:
# 	i = i.strip('\n')
# 	date, time, pid, label = i.split(',')
# 	temp_x = []
# 	temp_y = []

# 	temp_x.append(date)
# 	temp_x.append(time)
# 	temp_x.append(pid)
# 	temp_y.append(label)

# 	temp_data = []
# 	temp_x = np.asarray(temp_x, dtype=np.intc)
# 	temp_y = np.asarray(temp_y, dtype=np.intc)

# 	temp_data.append(temp_x)
# 	temp_data.append(temp_y)
# 	temp_data = np.asarray(temp_data)

# 	raw_data.append(temp_data)
# 	# raw_data.append(temp_x)
# 	# raw_data.append(temp_y)

# # x = np.asarray(x)
# raw_data = np.asarray(raw_data)
# np.save('raw_data.npy', raw_data)
# np.save('y.npy', y)