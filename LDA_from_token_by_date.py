# 출처 https://happy-obok.tistory.com/5
# https://radimrehurek.com/gensim/models/ldamodel.html
# https://wikidocs.net/30708

from collections import Counter
import pickle, csv, codecs
from gensim import corpora, models
import gensim
from gensim.models import LdaModel
from gensim.test.utils import datapath
from Data_Pre_processing_by_date import *

def LDA_model_from_token(text_file_name):
    token_file_name = text_file_name[:-4] + '.csv'
    print("loading "+token_file_name)
    data_word = []
    with codecs.open(token_file_name, 'r') as f:
        rdr = csv.reader(f)
        next(rdr)
        for i, line in enumerate(rdr):
            data_word.append(line)
        print("Complete loading")


    id2word=corpora.Dictionary(data_word)
    id2word.filter_extremes(no_below = 10) #10회 이하로 등장한 단어는 삭제
    texts = data_word
    corpus=[id2word.doc2bow(text) for text in texts]

    lda = LdaModel(corpus, num_topics=5, id2word=id2word)

    temp_file = datapath(token_file_name[:-4])
    lda.save(temp_file)

    lda = LdaModel.load(temp_file)

    topics = lda.print_topics(num_words=10)
    for topic in topics:
        print(topic)

standard_time1 = date_list.pop(0)
file_name1 = making_file_name(standard_time1)
LDA_model_from_token(file_name1)

standard_time2 = date_list.pop(0)
file_name2 = making_file_name(standard_time2)
LDA_model_from_token(file_name2)

standard_time3 = date_list.pop(0)
file_name3 = making_file_name(standard_time3)
LDA_model_from_token(file_name3)

standard_time4 = date_list.pop(0)
file_name4 = making_file_name(standard_time4)
LDA_model_from_token(file_name4)

standard_time5 = date_list.pop(0)
file_name5 = making_file_name(standard_time5)
LDA_model_from_token(file_name5)

standard_time6 = date_list.pop(0)
file_name6 = making_file_name(standard_time6)
LDA_model_from_token(file_name6)

standard_time7 = date_list.pop(0)
file_name7 = making_file_name(standard_time7)
LDA_model_from_token(file_name7)

standard_time8 = date_list.pop(0)
file_name8 = making_file_name(standard_time8)
LDA_model_from_token(file_name8)

standard_time9 = date_list.pop(0)
file_name9 = making_file_name(standard_time9)
LDA_model_from_token(file_name9)


"""

mallet_path = 'mallet-2.0.8/bin/mallet'
ldamallet = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=10, id2word=id2word)


# https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/07/09/lda/
# topic
K=9


# 각 토픽이 각 문서에 할당되는 횟수
# Counter로 구성된 리스트
# 각 Counter는 각 문서를 의미
print("counting documents topic")
document_topic_counts = [Counter() for _ in documents]

# 각 단어가 각 토픽에 할당되는 횟수
# Counter로 구성된 리스트
# 각 Counter는 각 토픽을 의미
print("Preprosessing topic modelling")
topic_word_counts = [Counter() for _ in range(K)]

# 각 토픽에 할당되는 총 단어수
# 숫자로 구성된 리스트
# 각각의 숫자는 각 토픽을 의미함
topic_counts = [0 for _ in range(K)]

# 각 문서에 포함되는 총 단어수
# 숫자로 구성된 리스트
# 각각의 숫자는 각 문서를 의미함
document_lengths = list(map(len, documents))

# 단어 종류의 수
distinct_words = set(word for document in documents for word in document)
V = len(distinct_words)

# 총 문서의 수
D = len(documents)

def p_topic_given_document(topic, d, alpha=0.1):
    # 문서 d의 모든 단어 가운데 topic에 속하는
    # 단어의 비율 (alpha를 더해 smoothing)
    return ((document_topic_counts[d][topic] + alpha) /
            (document_lengths[d] + K * alpha))

def p_word_given_topic(word, topic, beta=0.1):
    # topic에 속한 단어 가운데 word의 비율
    # (beta를 더해 smoothing)
    return ((topic_word_counts[topic][word] + beta) /
            (topic_counts[topic] + V * beta))

def topic_weight(d, word, k):
    # 문서와 문서의 단어가 주어지면
    # k번째 토픽의 weight를 반환
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)

def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k) for k in range(K)])

import random
def sample_from(weights):
    # i를 weights[i] / sum(weights)
    # 확률로 반환
    total = sum(weights)
    # 0과 total 사이를 균일하게 선택
    rnd = total * random.random()
    # 아래 식을 만족하는 가장 작은 i를 반환
    # weights[0] + ... + weights[i] >= rnd
    for i, w in enumerate(weights):
        rnd -= w
        if rnd <= 0:
            return i


random.seed(0)



# 각 단어를 임의의 토픽에 랜덤 배정
print("assigning word to topic in random")
document_topics = [[random.randrange(K) for word in document]
                    for document in documents]

# 위와 같이 랜덤 초기화한 상태에서
# AB를 구하는 데 필요한 숫자를 세어봄
for d in range(D):
    for word, topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][topic] += 1
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1
print("start topic modelling")
for iter in range(3):
    print(iter)
    for d in range(D):
        for i, (word, topic) in enumerate(zip(documents[d],
                                              document_topics[d])):
            # 깁스 샘플링 수행을 위해
            # 샘플링 대상 word와 topic을 제외하고 세어봄
            document_topic_counts[d][topic] -= 1
            topic_word_counts[topic][word] -= 1
            topic_counts[topic] -= 1
            document_lengths[d] -= 1

            # 깁스 샘플링 대상 word와 topic을 제외한
            # 말뭉치 모든 word의 topic 정보를 토대로
            # 샘플링 대상 word의 새로운 topic을 선택
            new_topic = choose_new_topic(d, word)
            document_topics[d][i] = new_topic

            # 샘플링 대상 word의 새로운 topic을 반영해
            # 말뭉치 정보 업데이트
            document_topic_counts[d][new_topic] += 1
            topic_word_counts[new_topic][word] += 1
            topic_counts[new_topic] += 1
            document_lengths[d] += 1

pickle_list = [document_topics, document_topic_counts, topic_word_counts, topic_counts]

f = open('document_topics.csv', 'w', newline="")
wr = csv.writer(f)
for word in document_topics:
    wr.writerow(word)
f.close()

with open('document_topic.pickle','wb') as fw:
    pickle.dump(pickle_list, fw)
    print("dumping complete")
    
    
"""