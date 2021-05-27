from gensim.models import LdaModel
from gensim.test.utils import datapath
import csv

temp_file = datapath("full_content_only")
lda = LdaModel.load(temp_file)


topics = lda.print_topics(num_words=20)

f = open("LDA_result.csv", 'w', newline="")
wr = csv.writer(f)
for topic in topics:
    wr.writerow(topic)
    print(topic)
f.close()
