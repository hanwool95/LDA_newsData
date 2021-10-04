#출처 https://wikidocs.net/31698
import pandas as pd # 데이터프레임 사용을 위해
from math import log # IDF 계산을 위해

import codecs, csv


def get_tf_idf(file_name):
    docs = []

    with codecs.open(file_name+'.csv', 'r') as f:
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

    f = open(file_name+'result.csv', 'w', newline="")
    wr = csv.writer(f)
    for key, value in sorted_result:
        wr.writerow([key, value[0], value[1]])
    f.close()

get_tf_idf('한겨레')
get_tf_idf('경향신문')
get_tf_idf('조선일보')
get_tf_idf('동아일보')
get_tf_idf('중앙일보')