import os
import re

realpath = os.path.dirname(os.path.realpath(__file__))

def _open_file(filename):
    filepath = realpath + "/negative/" + filename
    wordlist = list(open(filepath).read().splitlines())
    return wordlist


def _remove_words(sentence, words2remove):
    for word in words2remove:
        sentence = re.sub(r"\b" + word + r"\b", "", sentence.lower())
        sentence = re.sub(r"\s+", " ", sentence).strip()
    return sentence


# main cleansing function
def remove_stopwords_id(sentence):
    stopwords = _open_file("stopwords-id.txt")
    sentence = _remove_words(sentence, stopwords)
    return sentence


def remove_region_id(sentence):
    regions = _open_file("indonesian-region.txt")
    sentence = _remove_words(sentence, regions)
    return sentence


def remove_vulgarity_id(sentence):
    swears = _open_file("swear-words.txt")
    sentence = _remove_words(sentence, swears)
    return sentence
