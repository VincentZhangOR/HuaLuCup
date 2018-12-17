import sys
import matplotlib.pyplot as plt
import csv
from copy import deepcopy

f = sys.argv[1]

m = {1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31, 4:30, 6:30, \
		9:30, 11:30, 2:28}
aqi_map = {'优':1, '良':2, '轻度污染':3, '中度污染':4,'严重污染':5,'重度污染':6}

def cal_time(mon, day, hour):
	monN, dayN, hourN = int(mon), int(day), int(hour)
	cur = 4
	total = 0
	if monN >= 4:
		while monN > cur:
			total += m[cur] * 24
			cur += 1
		
	else:
		total += (30+31+30+31+31+30+31+30+31) * 24
		while monN > cur:
			total += m[cur] * 24
			cur += 1
	total += (dayN-1) * 24
	total += hourN
	return total

x = []
y_num = []
y_class = []

d = {}

for line in open(f).readlines():
	if '_' not in line:
		line.replace('c', '0')
		line.replace('C', '0')
		line = line.strip().split(' ')
		mon, day = line[0].split('-')[1:]
		hour = line[1].split(',')[0].split(':')[0]
		time_point = cal_time(mon,day,hour)
		# try:
		aqi = int(line[1].split(',')[3])
		aqi_class = line[1].split(',')[4]
		y_num.append(aqi)
		y_class.append(aqi_class)
		x.append(time_point)

		# d[time_point] = list(map(int, line[1].split(',')[6])) + [aqi] + [aqi_map[aqi_class]]
		assert len(line[1].split(',')) == 13
		d[time_point] = line[1].split(',')[6:] + [aqi] + [aqi_map[aqi_class]]
	# except:
	# 	print(aqi)
	# 	print(line)


d2 = {}

f2 = sys.argv[2]
for line in open(f2).readlines()[1:]:
	if '999999' in line:
		continue
	line.replace('c', '0')
	line.replace('C', '0')
	line = line.strip().strip(',').split(',')
	raw_time = line[2].split(' ')
	mon, day = raw_time[0].split('/')[1:]
	hour = raw_time[1].split(':')[0]
	time_point = cal_time(mon, day, hour)
	weather = line[3:]
	# try:
	d2[time_point] = weather


row = []
dd = deepcopy(d)
for t in sorted(dd.keys())[24:]:
	T = 1
	flag = 0
	out = []
	while T <=24:
		tt = 1
		while t-T not in d2:
			if t-T+tt in d2:
				d2[t-T] = d2[t-T+tt]
				break
			tt += 1
		tt = 1
		while t-T not in d:
			if t-T+tt in d:
				d[t-T] = d[t-T+tt]
				break
			tt += 1
			# flag = 1
			# break
		# else:
		out += d2[t-T] + d[t-T]
		T += 1
	if flag == 0:
		row.append([t%24]+out+[d[t][-2]])

with open('train_regression.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(row)
writeFile.close()



