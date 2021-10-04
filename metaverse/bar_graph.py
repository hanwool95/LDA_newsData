
from matplotlib import pyplot as plt

import csv, codecs, pickle

from datetime import datetime

from matplotlib import rc

rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

dict = {}

#to pickle
with codecs.open('metaverse_2.csv', 'r') as f:
    rdr = csv.reader(f)
    next(rdr)
    for line in rdr:
        journal = line[3]
        if journal in dict.keys():
            dict[line[3]] += 1
        else:
            dict[line[3]] = 1
print("searching data complete")

print(dict)


x_list = []
y_list = []

f = open('journal_count.csv', 'w', newline="")
wr = csv.writer(f)
for key, value in dict.items():
    wr.writerow([key, value])
    x_list.append(key)
    y_list.append(value)

f.close()

# drawing bar graph


print(x_list)
print(y_list)

plt.bar(x_list,y_list)
plt.title("신문사별 메타버스 기사 건")

plt.legend(['신문사', 'count'])

plt.show()
