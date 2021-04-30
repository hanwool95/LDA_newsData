#출처 https://github.com/lovit/soynlp#noun-extractor

from soynlp.noun import LRNounExtractor_v2
from soynlp.word import WordExtractor
import openpyxl
from soynlp.tokenizer import LTokenizer

import pandas as pd

import re, pickle, csv

from Data_Pre_processing_by_date import *

exception_list = ['있다', '수', '에', '이', '한다', '있습니다', '것으로', '있는', '것', '할', '및', 'the',
                  'http', 'https', 'sunday','joins','co','and', 'kr', '고', '것이다', '한', 'is', 'www', 'for', 'a', 'of',
                  'in', 'on', '중', '더', '대', '통해', '기자', '서울', '뉴시스', '재배포', '금지', '무단', '전재', '연합뉴',
                  '뉴7', '이번', '구독', '사진', '밝혔다', '저작권자', '네이버', '하지만', '이런', '그', '것이', '것은', 'pr', 'to',
                  'se', '부산일보', '연합뉴', 'de', 's', 'be', 'with', 'ha', 'en', 'an', 'PR', 'ac', 'ca', 'N', '로', '대한',
                  '등', '를', '위해', '말했', '그러나', '대해', '오후', '이데이일', 'edaily', '합니다' ,'위한', '내년', '올해',
                  '파이낸셜뉴스', '한국경제TV', '는', '의', '머니투데', '하는', '이는', 'this', 'it', 'The', 'that', 'will', 'as', 'by',
                  'fi']



standard_time1 = date_list.pop(0)
file_name1 = making_file_name(standard_time1)
f1 = open(file_name1, 'r')

standard_time2 = date_list.pop(0)
file_name2 = making_file_name(standard_time2)
f2 = open(file_name2, 'r')

standard_time3 = date_list.pop(0)
file_name3 = making_file_name(standard_time3)
f3 = open(file_name3, 'r')

standard_time4 = date_list.pop(0)
file_name4 = making_file_name(standard_time4)
f4 = open(file_name4, 'r')

standard_time5 = date_list.pop(0)
file_name5 = making_file_name(standard_time5)
f5 = open(file_name5, 'r')

standard_time6 = date_list.pop(0)
file_name6 = making_file_name(standard_time6)
f6 = open(file_name6, 'r')

standard_time7 = date_list.pop(0)
file_name7 = making_file_name(standard_time7)
f7 = open(file_name7, 'r')

standard_time8 = date_list.pop(0)
file_name8 = making_file_name(standard_time8)
f8 = open(file_name8, 'r')

standard_time9 = date_list.pop(0)
file_name9 = making_file_name(standard_time9)
f9 = open(file_name9, 'r')


print("loading scores_dictionary")
with open('noun_scores_dictionary.pickle', 'rb') as fr:
    scores_dictionary = pickle.load(fr)
    print("load complete")

def content_to_token(text_file_name):
    print("opening file " + text_file_name)
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

    token_file_name = text_file_name[:-4] + '.csv'

    f = open(token_file_name, 'w', newline="")
    wr = csv.writer(f)
    for word in words:
        wr.writerow(word)
    f.close()

content_to_token(file_name1)
content_to_token(file_name2)
content_to_token(file_name3)
content_to_token(file_name4)
content_to_token(file_name5)
content_to_token(file_name6)
content_to_token(file_name7)
content_to_token(file_name8)
content_to_token(file_name9)



f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()

# 전체로 한 다음에 토픽 보고. 연도 별로 변화하는 것을 본 다음에,
# 7에서 하면 토픽 이렇게 이룸 붙이고 12로 뽑으면 토픽 이렇게 나올 것 같
# 그 달에 나온 단어들 빈도수 보는 것.

