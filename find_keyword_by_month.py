
from matplotlib import pyplot as plt

import csv, codecs, pickle

from datetime import datetime
from soynlp.tokenizer import LTokenizer
from making_token_from_scores import *

date = "2002-07"

print("loading pickle")
with open('contents_by_month.pickle', 'rb') as fr:
    dict = pickle.load(fr)
    print("loading complete")

#print(dict.keys())


def make_content_text_file(month, list):
    title = "month"+month+".txt"
    f = open(title, 'w')
    for line in list:
        data = line + "\n"
        f.write(data)
    f.close()

def count_key_word_in_token(month):
    title = "month"+month+".csv"
    #print("loading " + title)
    data_word = {}
    #print("counting key words in " + title)
    with codecs.open(title, 'r') as f:
        rdr = csv.reader(f)
        next(rdr)
        for i, line in enumerate(rdr):
            for word in line:
                if word in word_dict.keys():
                    w = word_dict[word]
                else:
                    w = word

                if w in data_word.keys():
                    data_word[w] += 1
                else:
                    data_word[w] = 1

    def f1(x):
        return x[1]

    sorted_dict = sorted(data_word.items(), key=f1, reverse=True)

    return sorted_dict


def extract_key_word_in_month(month):
    title = "month"+month+".txt"
    make_content_text_file(month, dict[month])
    content_to_token(title)
    sorted_word_dict = count_key_word_in_token(month)
    print(month+" key word top 20 list")
    print(sorted_word_dict[:20])

if __name__ == '__main__':
    extract_key_word_in_month("2002-07")
    extract_key_word_in_month("2005-11")
    extract_key_word_in_month("2009-03")
    extract_key_word_in_month("2013-10")
    extract_key_word_in_month("2015-11")
    extract_key_word_in_month("2016-04")
    extract_key_word_in_month("2016-09")
    extract_key_word_in_month("2017-12")
    extract_key_word_in_month("2020-01")