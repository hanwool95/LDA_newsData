# 출처 https://techrando.com/2019/08/14/a-brief-introduction-to-change-point-detection-using-python/

import csv, codecs, pickle

from datetime import datetime

import matplotlib.pyplot as plt
import ruptures as rpt

import numpy as np



with open('date_count.pickle', 'rb') as fr:
    sorted_dict = pickle.load(fr)

#for tuple in sorted_dict:
#    print(tuple)

#print(sorted_dict)

x_list = []
y_list = []

start_date = "1990.01"
last_date = "2021.06"

for tuple in sorted_dict:
    if tuple[0] >= start_date and tuple[0] <= last_date:
        x_obj = datetime.strptime(tuple[0], '%Y.%m')
        x_list.append(x_obj)
        y_list.append(tuple[1])

#print(x_list)
#print(y_list)

points=np.array(y_list)

# detection using pelt method
algo = rpt.Pelt(model="rbf").fit(points)
result = algo.predict(pen=2)


label_list = []

print(result)
for index in result:
    label_list.append(x_list[index-1])
    #print(x_list[index])
label_list.pop()


plt.plot(x_list,y_list)
plt.title("Ai journal change point detection. Pelt model. 1990.01 - 2021.02")

for i, v in enumerate(x_list):
    if v in label_list:
        label = str(v.year) + "." + str(v.month)
        plt.text(v, y_list[i]+5000, label,       # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                 fontsize = 8,
                 color='black',
                 horizontalalignment='right',  # horizontalalignment (left, center, right)
                 verticalalignment='top')    # verticalalignment (top, center, bottom)
        plt.axvline(v, 0, 1, color='lightgray', linestyle=':', linewidth='2')


#plt.legend(['Date', 'count'])

plt.show()