from Data_Pre_processing_by_date import *
from gensim.models import LdaModel
from gensim.test.utils import datapath
from gensim import corpora
import csv


topic_dictionary = {}

def make_topic_dictionary():
    with codecs.open('topic_word.csv', 'r') as f:
        rdr = csv.reader(f)
        next(rdr)
        for i, line in enumerate(rdr):
            if line[0] in topic_dictionary.keys():
                topic_dictionary[line[0]].append([line[1], line[2]])
            else:
                topic_dictionary[line[0]] = [[line[1], line[2]]]
        print("Complete loading")

make_topic_dictionary()

def get_topic_from_token(text_file_name):
    token_file_name = text_file_name[:-4] + '.csv'
    print("loading " + token_file_name)
    topic_count = [0,0,0,0,0,0,0,0,0,0]
    with codecs.open(token_file_name, 'r') as f:
        rdr = csv.reader(f)
        next(rdr)
        count = 0
        for i, line in enumerate(rdr):
            count += 1
            scores_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for word in line:
                if word in topic_dictionary.keys():
                    data_list = topic_dictionary[word]
                    if len(data_list) < 2:
                        scores_list[int(data_list[0][0])] += float(data_list[0][1])
                    else:
                        scores_list[int(data_list[0][0])] += float(data_list[0][1])
                        scores_list[int(data_list[1][0])] += float(data_list[1][1])
            if max(scores_list) != 0:
                topic = scores_list.index(max(scores_list))
                topic_count[topic] += 1
    topic_percentage = []
    for t in topic_count:
        topic_percentage.append(round(t/count*100, 2))
    print(topic_percentage)

if __name__ == '__main__':

    standard_time1 = date_list.pop(0)
    file_name1 = making_file_name(standard_time1)
    get_topic_from_token(file_name1)

    standard_time2 = date_list.pop(0)
    file_name2 = making_file_name(standard_time2)
    get_topic_from_token(file_name2)

    standard_time3 = date_list.pop(0)
    file_name3 = making_file_name(standard_time3)
    get_topic_from_token(file_name3)

    standard_time4 = date_list.pop(0)
    file_name4 = making_file_name(standard_time4)
    get_topic_from_token(file_name4)

    standard_time5 = date_list.pop(0)
    file_name5 = making_file_name(standard_time5)
    get_topic_from_token(file_name5)

    standard_time6 = date_list.pop(0)
    file_name6 = making_file_name(standard_time6)
    get_topic_from_token(file_name6)

    standard_time7 = date_list.pop(0)
    file_name7 = making_file_name(standard_time7)
    get_topic_from_token(file_name7)

    standard_time8 = date_list.pop(0)
    file_name8 = making_file_name(standard_time8)
    get_topic_from_token(file_name8)

    standard_time9 = date_list.pop(0)
    file_name9 = making_file_name(standard_time9)
    get_topic_from_token(file_name9)

    standard_time10 = date_list.pop(0)
    file_name10 = making_file_name(standard_time10)
    get_topic_from_token(file_name10)
