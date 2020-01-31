import os
import re

realpath = os.path.dirname(os.path.realpath(__file__))
stopwords_dir = realpath + '/stopwords_id.txt'

stopwords = list(open(stopwords_dir).read().splitlines())

def remove_stopwords_id(sentence):
    for w in stopwords:
        sentence = re.sub(r'\b'+w+r'\b', '', sentence)
        sentence = re.sub(r'\s+', ' ', sentence).strip()
    return sentence