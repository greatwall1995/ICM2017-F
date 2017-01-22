import csv
import matplotlib.pyplot as plt
import numpy as np

cnt_age = [0] * 25
cnt_salary = [0] * 25

with open('data.csv', 'r') as f:
	data = csv.reader(f, delimiter = ',')
	cnt = 1
	for row in data:
		if int(row[3]) > 0:
			age = int(row[3])
			cnt_age[age] += 1
			cnt_salary[age] += int(row[1])

X = []
Y = []
for i in range(25):
	if cnt_age[i] > 0:
		X.append(i)
#		Y.append(1. * cnt_salary[i] / cnt_age[i])
		Y.append(cnt_age[i])
X = np.array(X)
Y = np.array(Y)
plt.plot(X, Y)
plt.show()