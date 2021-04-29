#출처 https://github.com/lovit/soynlp#noun-extractor

from soynlp.noun import LRNounExtractor_v2
from soynlp.word import WordExtractor
import openpyxl
from soynlp.tokenizer import LTokenizer

import pandas as pd

import re, pickle, csv

print("opening file")
with open('full_content_only.txt', 'r', encoding = "utf-8") as f:
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

exception_list = ['있다', '수', '에', '이', '한다', '있습니다', '것으로', '있는', '것', '할', '및', 'the',
                  'http', 'https', 'sunday','joins','co','and', 'kr', '고', '것이다', '한', 'is', 'www', 'for', 'a', 'of',
                  'in', 'on', '중', '더', '대', '통해']
## noun score
# 명사만한
noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=False)  # 복합어 추출 X
nouns = noun_extractor.train_extract(text)  # list of str like
noun_scores = {noun: score.score for noun, score in nouns.items()}
print("extracting noun")


ltokenizer = LTokenizer(scores = noun_scores)

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

f = open('noun_token_words_4.csv', 'w', newline="")
wr = csv.writer(f)
for word in words:
    wr.writerow(word)
f.close()

