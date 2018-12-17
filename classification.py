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

def train(XY, C, epoch):
	X, Y = zip(* XY)
	# models
	classifier_models = dict()
	classifier_models['GBClassifier'] = ensemble.GradientBoostingClassifier()
	classifier_models['RandomForestClassifier'] = ensemble.RandomForestClassifier()
	classifier_models['AdaBoostClassifier'] = ensemble.AdaBoostClassifier()
	classifier_models['DecisionTreeClassifier'] = tree.DecisionTreeClassifier()
	# classifier_models['GaussianNBClassifier'] = naive_bayes.GaussianNB()
	classifier_models['KNNClassifier'] = neighbors.KNeighborsClassifier()
	classifier_models['MLPClassifier'] = neural_network.MLPClassifier()
	classifier_models['SGDClassifier'] = linear_model.SGDClassifier(n_iter=epoch,verbose=0)
	# classifier_models['SVClinearClassifier'] = svm.SVC(kernel = 'linear', C=C)

	for name in classifier_models:
		print('----------------', name, '----------------')
		sys.stdout.flush()
		start = time()
		scores = cross_validation.cross_val_score(classifier_models[name], X, Y, cv=5)
		end = time()
		print('running time:', end - start)
		print(scores)
		mean, std = '{:.2%}'.format(scores.mean()), '{:.2%}'.format(scores.std())
		print(mean, std)
		print('\n')
		sys.stdout.flush()


if __name__ == '__main__':
	# trainfile = sys.argv[1]
	# testfile = sys.argv[2]
	totalfile = 'train.csv'
	epoch = int(sys.argv[1])
	# trainX, trainY = readfile(trainfile)
	# testX, testY = readfile(testfile)
	X, Y = readfile(totalfile)
	XY = list(zip(X,Y))
	random.shuffle(XY)
	train(XY, C, epoch)


