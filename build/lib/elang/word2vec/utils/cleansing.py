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
    """remove_stopwords_id Removes Bahasa Indonesia Stopwords
 
    Stopwords are generally the most common "function" words in a language, and they're routinely eliminated in natural language processing tasks.
    Bahasa Indonesia stopwords (eg. "ya", "kan", "dong", "loh") are removed from the input string.
    
    :param sentence: An input string
    :type sentence: str
    :return: A string where common Bahasa Indonesia stopwords are filtered out 
    :rtype: str
    """
    stopwords = _open_file("stopwords-id.txt")
    sentence = _remove_words(sentence, stopwords)
    return sentence


def remove_region_id(sentence):
    """remove_region_id Removes name of places in Indonesia 
    Regions are name of places (provinces and cities) in Indonesia (eg. "Jakarta", "Bali", "Sukabumi")
    
    :param sentence: An input string
    :type sentence: str
    :return: A string where common name of places in Indonesia are filtered out 
    :rtype: str
    """
    regions = _open_file("indonesian-region.txt")
    sentence = _remove_words(sentence, regions)
    return sentence


def remove_vulgarity_id(sentence):
    """remove_vulgarity_id Removes uncivilised words in Bahasa Indonesia 
    Prevent words such as "anjir", "babi" etc to be included in natual language generation tasks
    
    :param sentence: An input string
    :type sentence: str
    :return: A string where common swear words in Indonesia are filtered out 
    :rtype: str
    """
    swears = _open_file("swear-words.txt")
    sentence = _remove_words(sentence, swears)
    return sentence

def remove_calendar_id(sentence):
    """remove_datetime_id Removes common "calendar words" in Bahasa Indonesia 
    Calendar words include day of weeks (eg. senin, selasa, ...), months (`maret`, 'juni'), and their abbreviated forms (`okt`, 'jul') 

    :param sentence: An input string
    :type sentence: str
    :return: A string where calendar words in Indonesia are filtered out 
    :rtype: str
    """
    swears = _open_file("calendar-words.txt")
    sentence = _remove_words(sentence, swears)
    return sentence
