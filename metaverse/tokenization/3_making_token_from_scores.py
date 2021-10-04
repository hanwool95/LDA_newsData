#출처 https://github.com/lovit/soynlp#noun-extractor

from soynlp.noun import LRNounExtractor_v2
from soynlp.word import WordExtractor
import openpyxl
from soynlp.tokenizer import LTokenizer

import pandas as pd

import re, pickle, csv

exception_list = ['있다', '수', '에', '이', '한다', '있습니다', '것으로', '있는', '것', '할', '및', 'the',
                  'http', 'https', 'sunday','joins','co','and', 'kr', '고', '것이다', '한', 'is', 'www', 'for', 'a', 'of',
                  'in', 'on', '중', '더', '대', '통해', '기자', '서울', '뉴시스', '재배포', '금지', '무단', '전재', '연합뉴',
                  '뉴7', '이번', '구독', '사진', '밝혔다', '저작권자', '네이버', '하지만', '이런', '그', '것이', '것은', 'pr', 'to',
                  'se', '부산일보', '연합뉴', 'de', 's', 'be', 'with', 'ha', 'en', 'an', 'PR', 'ac', 'ca', 'N', '로', '대한',
                  '등', '를', '위해', '말했', '그러나', '대해', '오후', '이데이일', 'edaily', '합니다' ,'위한', '내년', '올해',
                  '파이낸셜뉴스', '한국경제TV', '는', '의', '머니투데', '하는', '이는', 'this', 'it', 'The', 'that', 'will', 'as', 'by',
                  'fi', '의', '가', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다',
                  '등을', '했다', '경우', '을', '또', '등이', '지난', '말했다', '다양', '사용', '머니투데이', '지난해', '며', '게', '때',
                  '때문', '만들어', '전자신문', '며', '나타', '지금', '많이', '하고', '같은', '뉴스1', 'news1', '뉴스', '메인에서', 'news',
                  '이데일리', '오전', '헤럴드경제', '했습니다', '다른', '그는', '가장', 'her', '노컷뉴스', 'yna', '만나보세요', '오늘', '바로',
                  '달라진', '확', '흥', 'YTN', '있도', '전', '없다', '없는', '큰', '어떤', '제보', '국민일보', '1', '2', '3', '4',
                  '5', '6', '7', '8', '9', '10', '따라', '있다는', '것을', '오는', '아이뉴스24']

word_dict = {'서비': '서비스', '살처': '살처분', '네트워':'네트제워크', '데이':'데이터', '콘텐':'콘텐츠', '디자':'디자인', 'SK텔레':'SK텔레콤',
             'LG유플러': 'LG유플러스'}


text_file = 'full_content_only.txt'

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
            word = LR_list[0]
            if word in word_dict:
                word = word_dict[word]
            if word not in exception_list:
                conclude_sent.append(word)
        words.append(conclude_sent)

    token_file_name = text_file_name[:-4] + '.csv'

    f = open(token_file_name, 'w', newline="")
    wr = csv.writer(f)
    for word in words:
        wr.writerow(word)
    f.close()

if __name__ == '__main__':
    content_to_token(text_file)




# 전체로 한 다음에 토픽 보고. 연도 별로 변화하는 것을 본 다음에,
# 7에서 하면 토픽 이렇게 이룸 붙이고 12로 뽑으면 토픽 이렇게 나올 것 같
# 그 달에 나온 단어들 빈도수 보는 것.

