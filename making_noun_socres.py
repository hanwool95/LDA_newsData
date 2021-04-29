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

## noun score
# 명사만한
noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=False)  # 복합어 추출 X
nouns = noun_extractor.train_extract(text)  # list of str like
noun_scores = {noun: score.score for noun, score in nouns.items()}

with open('noun_scores_dictionary.pickle','wb') as fw:
    pickle.dump(noun_scores, fw)
    print("dumping complete")
