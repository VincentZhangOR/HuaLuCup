import random
import csv

f = 'aqi.csv'
f_train = 'aqi.train.csv'
f_test = 'aqi.test.csv'

l_train, l_test = [], []

# for i, line in enumerate(open(f).readlines()):
# 	r = random.randint(1,10)
# 	if r <= 8:
# 		l_train.append(line)
# 	else:
# 		l_test.append(line)
with open(f, 'r') as readFile:
	reader = csv.reader(readFile)
	lines = list(reader)
	for line in lines:
		r = random.randint(1,10)
		if r <= 8:
			l_train.append(line)
		else:
			l_test.append(line)
readFile.close()

with open(f_train, 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(l_train)
writeFile.close()


with open(f_test, 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(l_test)
writeFile.close()
