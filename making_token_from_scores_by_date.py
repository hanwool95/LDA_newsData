#출처 https://github.com/lovit/soynlp#noun-extractor

from soynlp.noun import LRNounExtractor_v2
from soynlp.word import WordExtractor
import openpyxl
from soynlp.tokenizer import LTokenizer

import pandas as pd

import re, pickle, csv

from Data_Pre_processing_by_date import *
from making_token_from_scores import *




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

