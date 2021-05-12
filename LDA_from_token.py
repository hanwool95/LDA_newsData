# 출처 https://happy-obok.tistory.com/5
# https://radimrehurek.com/gensim/models/ldamodel.html
# https://wikidocs.net/30708

from collections import Counter
import pickle, csv, codecs
from gensim import corpora, models
import gensim
from gensim.models import LdaModel
from gensim.test.utils import datapath
from making_token_from_scores import *

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

    lda = LdaModel(corpus, num_topics=10, id2word=id2word)

    temp_file = datapath(token_file_name[:-4])
    lda.save(temp_file)

    lda = LdaModel.load(temp_file)

    topics = lda.print_topics(num_words=10)
    for topic in topics:
        print(topic)

LDA_model_from_token(text_file)