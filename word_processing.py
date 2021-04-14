
from soynlp.noun import LRNounExtractor_v2
from soynlp.word import WordExtractor
import openpyxl

import pandas as pd

import re, pickle


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

# word_score
word_extractor = WordExtractor(min_frequency = 5)
word_extractor.train(text)
print("train word_extractor complete")
words_scores = word_extractor.extract()
print('complete to extract words_scores')

scores_dictionary = {'words_scores': words_scores, 'noun_scores': [], 'text': text}

with open('scores_dictionary.pickle','wb') as fw:
    pickle.dump(scores_dictionary, fw)
    print("dumping complete")

with open('scores_dictionary.pickle', 'rb') as fr:
    scores_dictionary = pickle.load(fr)
    print("loading complete")

## noun score

# 명사만
noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=False)  # 복합어 추출 X
nouns = noun_extractor.train_extract(text)  # list of str like
noun_scores = {noun: score.score for noun, score in nouns.items()}
print("extracting noun")

#print(list(noun_extractor._compounds_components.items())[:5])

scores_dictionary['noun_scores'] = noun_scores

with open('scores_dictionary.pickle','wb') as fw:
    pickle.dump(scores_dictionary, fw)
    print("dumping complete")


"""

Noun = []
for noun, score in nouns.items():
    Noun.append(noun)

# 저장
noun_df = pd.DataFrame({'words': Noun})
noun_df.to_excel("nouns.xlsx")

"""