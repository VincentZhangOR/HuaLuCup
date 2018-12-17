import random
import sys
import csv

f = sys.argv[1]

train, test = [], []

with open(f, 'r') as readFile:
	reader = csv.reader(readFile)
	lines = list(reader)
	for line in lines:
		r = random.randint(1,10)
		if r <= 8:
			train.append(line)
		else:
			test.append(line)
readFile.close()

with open('zhongshannorth.train.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(train)
writeFile.close()

with open('zhongshannorth.test.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(test)
writeFile.close()