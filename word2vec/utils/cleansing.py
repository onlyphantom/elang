import os
import re

realpath = os.path.dirname(os.path.realpath(__file__))

# helper function
def open_file(filename):
    filepath = realpath + "/" + filename
    wordlist = list(open(filepath).read().splitlines())
    return wordlist

def remove_words(sentence, words2remove):
    for word in words2remove:
        sentence = re.sub(r'\b' + word + r'\b', '', sentence.lower())
        sentence = re.sub(r'\s+', ' ', sentence).strip()
    return sentence

# main cleansing function
def remove_stopwords_id(sentence):
    stopwords = open_file("stopwords-id.txt")
    sentence = remove_words(sentence, stopwords)
    return sentence

def remove_region_id(sentence):
    regions = open_file("indonesian-region.txt")
    sentence = remove_words(sentence, regions)
    return sentence

def remove_vulgarity_id(sentence):
    swears = open_file("swear-words.txt")
    sentence = remove_words(sentence, swears)
    return sentence