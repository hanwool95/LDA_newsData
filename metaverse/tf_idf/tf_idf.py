#출처 https://wikidocs.net/31698
import pandas as pd # 데이터프레임 사용을 위해
from math import log # IDF 계산을 위해

import codecs, csv

docs = []

with codecs.open('full_content_only.csv', 'r') as f:
    rdr = csv.reader(f)
    next(rdr)
    for line in rdr:
        docs.append(line)

N = len(docs) # 총 문서의 수

def tf(t, d):
    return d.count(t)

def idf(t):
    df = 0
    for doc in docs:
        df += t in doc
    return log(N/(df + 1))

def tfidf(t, d):
    return tf(t,d)* idf(t)

result = {}

for line in docs: # 각 문서에 대해서 아래 명령을 수행
    for word in line:
        result[word] = [tf(word, line), idf(word)]

sorted_result = sorted(result.items(),
                              reverse=True,
                              key=lambda item: item[1][1])

f = open('result_tf_idf', 'w', newline="")
wr = csv.writer(f)
for key, value in sorted_result:
    wr.writerow([key, value[0], value[1]])
f.close()
