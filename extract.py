import csv

fs = ['2017-04.csv', '2017-05.csv', '2017-06.csv', '2017-07.csv', '2017-08.csv', '2017-09.csv', '2017-10.csv', '2017-11.csv', '2017-12.csv', '2018-02.csv', '2018-02.csv', '2018-03.csv']

out = []
visited = set()

# for f in fs:
	# for line in open(f).readlines():
	# 	line = line.strip().split(',')
	# 	firstline = line[0].split(' ')
	# 	if line[1] == '天津':
	# 		out.append(firstline+line[1:])
f = 'aqi.csv'
with open(f, 'r') as readFile:
	reader = csv.reader(readFile)
	lines = list(reader)
	for line in lines:
		# print(line[1])
		if line[1] == '天津' and line[2] == '中山北路':
			if tuple(line) not in visited:
				out.append(line)
				visited.add(tuple(line))

with open('aqi.zhongshannorth.csv', 'a') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(out)

readFile.close()
writeFile.close()
