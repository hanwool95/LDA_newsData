from gensim.models import LdaModel
from gensim.test.utils import datapath

temp_file = datapath("noun_model")
lda = LdaModel.load(temp_file)


topics = lda.print_topics(num_words=20)
for topic in topics:
    print(topic)
