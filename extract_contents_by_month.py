
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
            dict[date].append(line[5])
        else:
            dict[date] = [line[5]]
print("searching data complete")



with open('contents_by_month.pickle','wb') as fw:
    pickle.dump(dict, fw)
    print("dumping complete")


