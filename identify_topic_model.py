from gensim.models import LdaModel
from gensim.test.utils import datapath

temp_file = datapath("full_content_only")
lda = LdaModel.load(temp_file)


topics = lda.print_topics(num_words=20)
for topic in topics:
    print(topic)
