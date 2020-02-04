import os
import re
from gensim.utils import simple_preprocess

realpath = os.path.dirname(os.path.realpath(__file__))
file_dir = realpath + '/simple_preprocess/sentences.txt'
stopwords_dir = realpath + '/utils/stopwords_id.txt'
# with open(file_dir, 'r') as reader:
#     for sentence in reader.readlines():
#         print(sentence, end='')

stopwords = list(open(stopwords_dir).read().splitlines())

def remove_stopwords(sentence):
    for w in stopwords:
        sentence = re.sub(r'\b'+w+r'\b', '', sentence)
        sentence = re.sub(r'\s+', ' ', sentence).strip()
    return sentence

sentences = list(map(remove_stopwords, open(file_dir).read().splitlines()))
corpus = list(map(simple_preprocess, sentences))
print(corpus[:2], "\nSentences: -->", len(corpus))
uniqset = set(word for l in corpus for word in l) 
print(len(uniqset), "Unique Terms")


# corpus = list(map(simple_preprocess, open(file_dir).read().splitlines()))
# print(corpus[-6:], "\nSentences: -->", len(corpus))
# uniqset = set(word for l in corpus for word in l) 
# print(len(uniqset), "Unique Terms")
