
from soynlp.noun import LRNounExtractor_v2
from soynlp.word import WordExtractor
import openpyxl
from soynlp.tokenizer import LTokenizer

import pandas as pd

import re, pickle, csv


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

## noun score

# 명사만
noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=False)  # 복합어 추출 X
nouns = noun_extractor.train_extract(text)  # list of str like
noun_scores = {noun: score.score for noun, score in nouns.items()}
print("extracting noun")

#print(list(noun_extractor._compounds_components.items())[:5])

ltokenizer = LTokenizer(scores = noun_scores)

print("making list of words")
words = [ltokenizer.tokenize(sent) for sent in text]
word_list = []

f = open('noun_token_words.csv', 'w', newline="")
wr = csv.writer(f)
for word in words:
    wr.writerow(word)
    word_list.append(word)
f.close()

with open('noun_token_word_list.pickle','wb') as fw:
    pickle.dump(word_list, fw)
    print("dumping complete")


