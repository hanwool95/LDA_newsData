#출처 https://github.com/lovit/soynlp#noun-extractor

from soynlp.noun import LRNounExtractor_v2
from soynlp.word import WordExtractor
import openpyxl
from soynlp.tokenizer import LTokenizer

import pandas as pd

import re, pickle, csv

text_file_name = 'full_content_only.txt' #open
token_file_name = 'noun_token_words_5.csv' #save

exception_list = ['있다', '수', '에', '이', '한다', '있습니다', '것으로', '있는', '것', '할', '및', 'the',
                  'http', 'https', 'sunday','joins','co','and', 'kr', '고', '것이다', '한', 'is', 'www', 'for', 'a', 'of',
                  'in', 'on', '중', '더', '대', '통해']


print("loading scores_dictionary")
with open('noun_scores_dictionary.pickle', 'rb') as fr:
    scores_dictionary = pickle.load(fr)
    print("load complete")

print("opening file")
with open(text_file_name, 'r', encoding = "utf-8") as f:
    lines = f.read().splitlines()
re.sub(r"[\[\]<>~]", ' ', lines[0])
re.sub(r"['~]", ' ', lines[0])
re.sub(r'"', ' ', lines[0])

text = []
for line in lines:
    line = re.sub(r"[\[\]<>~]", ' ', line)
    line = re.sub(r"['~]", ' ', line)
    line = re.sub(r'"', ' ', line)
    line = re.sub('\\W', ' ', line)
    text.append(line)


ltokenizer = LTokenizer(scores = scores_dictionary)

print("making list of words")
words = []
for sent in text:
    conclude_sent = []
    #flatten을 False로 주어서 [L명사, R조사]형태로 분류하게 만듦.
    pre_list = ltokenizer.tokenize(sent, flatten=False)
    for LR_list in pre_list:
        if LR_list[0] not in exception_list:
            conclude_sent.append(LR_list[0])
    words.append(conclude_sent)

f = open(token_file_name, 'w', newline="")
wr = csv.writer(f)
for word in words:
    wr.writerow(word)
f.close()

