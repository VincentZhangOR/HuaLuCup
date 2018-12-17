import sys
import matplotlib.pyplot as plt

f = sys.argv[1]

m = {1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31, 4:30, 6:30, \
		9:30, 11:30, 2:28}

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
y = []

for line in open(f).readlines():
	line = line.strip().split(' ')
	mon, day = line[0].split('-')[1:]
	hour = line[1].split(',')[0].split(':')[0]
	time_point = cal_time(mon,day,hour)
	try:
		aqi = int(line[1].split(',')[3])
		y.append(aqi)
		x.append(time_point)
	except:
		print(aqi)
		print(line)
	
assert len(x) == len(y)

# print(y)

plt.plot(x, y)
plt.show()

