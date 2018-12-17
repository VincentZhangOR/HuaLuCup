from sklearn import *
import sys
import numpy as np
import random
from time import time

def readfile(filename):
	X, Y = [], []
	for i,line in enumerate(open(filename).readlines()):
		line = line.replace('C', '0')
		line = line.replace('/', '0')
		line = line.strip().split(',')
		if len(line) == 386:
			X.append(list(map(float, line[:-1])))
			Y.append(int(line[-1]))
	return X, Y

def train(XY, epoch):
	X, Y = zip(* XY)
	# models
	regressor_models = dict()
	regressor_models['LinearRegressor'] = linear_model.LinearRegression()
	regressor_models['AdaBoostRegressor'] = ensemble.AdaBoostRegressor()
	regressor_models['RandomForestRegressor'] = ensemble.RandomForestRegressor(n_estimators=100, criterion='mse', random_state=1, n_jobs=-1)
	# regressor_models['SGDRegressor'] = linear_model.SGDRegressor(n_iter=epoch)
	regressor_models['MLPRegressor'] = neural_network.MLPRegressor()
	regressor_models['DecisionTreeRegressor'] = tree.DecisionTreeRegressor()
	regressor_models['KNNRegressor'] = neighbors.KNeighborsRegressor()

	for name in regressor_models:
		print('----------------', name, '----------------')
		sys.stdout.flush()
		
		start = time()
		scores = cross_validation.cross_val_score(regressor_models[name], X, Y, cv=5)
		end = time()
		print('running time:', end - start)
		print(scores)
		mean, std = '{:.2%}'.format(scores.mean()), '{:.2%}'.format(scores.std())
		print('mean:', mean, 'std:', std)

		X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size = 0.3)
		regressor_models[name].fit(X_train, Y_train)
		Y_train_predict = regressor_models[name].predict(X_train)
		MSE_train = metrics.mean_squared_error(Y_train, Y_train_predict)
		Y_test_predict = regressor_models[name].predict(X_test)
		MSE_test = metrics.mean_squared_error(Y_test, Y_test_predict)
		print('MSE_train:','{:.2f}'.format(MSE_train), 'MSE_test:', '{:.2f}'.format(MSE_test))
		print('\n')
		sys.stdout.flush()


if __name__ == '__main__':
	# trainfile = sys.argv[1]
	# testfile = sys.argv[2]
	totalfile = 'train_regression.csv'
	epoch = int(sys.argv[1])
	# trainX, trainY = readfile(trainfile)
	# testX, testY = readfile(testfile)
	X, Y = readfile(totalfile)
	XY = list(zip(X,Y))
	random.shuffle(XY)
	train(XY, epoch)


