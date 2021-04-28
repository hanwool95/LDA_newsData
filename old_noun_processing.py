#출처 https://github.com/lovit/soynlp#noun-extractor

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
#word_list = []

f = open('noun_token_words_2.csv', 'w', newline="")
wr = csv.writer(f)
for word in words:
    w_list = []
    for w in word:
        word_is_noun = 0
        try:
            word_is_noun = noun_scores[w]
        except:
            print(w)
        if word_is_noun > 0.5:
            w_list.apppend(w)
    wr.writerow(w_list)
            #word_list.append(word)
f.close()



#with open('noun_token_word_list.pickle','wb') as fw:
#    pickle.dump(word_list, fw)
#    print("dumping complete")

