from gensim.utils import simple_preprocess
import os

file_dir = os.path.dirname(os.path.realpath(__file__)) + '/simple_preprocess/sentences.txt'
# with open(file_dir, 'r') as reader:
#     for sentence in reader.readlines():
#         print(sentence, end='')

corpus = list(map(simple_preprocess, open(file_dir).read().splitlines()))
print(corpus[-6:], "\nSentences: -->", len(corpus))
uniqset = set(word for l in corpus for word in l) 
print(len(uniqset), "Unique Terms")
