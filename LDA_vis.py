#출처 https://wikidocs.net/30708

import pyLDAvis.gensim_models

from gensim.models import LdaModel
from gensim import corpora, models
from gensim.test.utils import datapath

import codecs, csv

file_name = 'previous/content2002_9.csv'

def LDA_to_vis(text_file_name):
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


    temp_file = datapath(token_file_name[:-4])
    lda = LdaModel.load(temp_file)

    pyLDAvis.enable_notebook()
    vis = pyLDAvis.gensim_models.prepare(lda, corpus, id2word)
    pyLDAvis.display(vis)

LDA_to_vis(file_name)