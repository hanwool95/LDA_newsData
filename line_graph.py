
from matplotlib import pyplot as plt

import csv, codecs, pickle

from datetime import datetime

"""
dict = {}

#to pickle
with codecs.open('full_data.csv', 'r') as f:
    rdr = csv.reader(f)
    next(rdr)
    for line in rdr:
        date = line[2][:7]
        if date in dict.keys():
            dict[date] += 1
        else:
            dict[date] = 0
print("searching data complete")


def f1(x):
    return x[0]

sorted_dict = sorted(dict.items(), key=f1)
print("complete sorting data")


with open('date_count.pickle','wb') as fw:
    pickle.dump(sorted_dict, fw)
    print("dumping complete")

"""

with open('date_count.pickle', 'rb') as fr:
    sorted_dict = pickle.load(fr)


f = open('date_count.csv', 'w', newline="")
wr = csv.writer(f)
for tuple in sorted_dict:
    wr.writerow([tuple[0], tuple[1]])
f.close()

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

print(x_list)
print(y_list)

plt.plot(x_list,y_list)
plt.title("1990.01 - 2021.02")

label_list =[datetime(2005, 11, 1, 0, 0), datetime(2006, 11, 1, 0, 0), datetime(2008, 4, 1, 0, 0),
             datetime(2011, 1, 1, 0, 0), datetime(2013, 4, 1, 0, 0), datetime(2014, 1, 1, 0, 0),
             datetime(2016, 3, 1, 0, 0), datetime(2017, 1, 1, 0, 0), datetime(2018, 1, 1, 0, 0),
             datetime(2018, 10, 1, 0, 0), datetime(2019, 7, 1, 0, 0), datetime(2020, 12, 1, 0, 0)]

for i, v in enumerate(x_list):
    if v in label_list:
        label = str(v.year) + "." + str(v.month)
        plt.text(v, y_list[i], label,       # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                 fontsize = 9,
                 color='blue',
                 horizontalalignment='center',  # horizontalalignment (left, center, right)
                 verticalalignment='bottom')    # verticalalignment (top, center, bottom)

plt.legend(['Date', 'count'])

plt.show()