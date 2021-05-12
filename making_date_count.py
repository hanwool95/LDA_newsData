
from matplotlib import pyplot as plt

import csv, codecs, pickle

from datetime import datetime


dict = {}

#to pickle
with codecs.open('full_data_rev3.csv', 'r') as f:
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

with open('date_count.pickle', 'rb') as fr:
    sorted_dict = pickle.load(fr)

f = open('date_count.csv', 'w', newline="")
wr = csv.writer(f)
for tuple in sorted_dict:
    wr.writerow([tuple[0], tuple[1]])
f.close()

#print(sorted_dict)