import os
from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
from utils import remove_stopwords_id

REAL_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_DIR = REAL_PATH + '/simple_preprocess/sentences.txt'
MODEL_DIR = REAL_PATH + '/model/fin.model'
SIZE= 100
WINDOW = 5
ITER = 10
WORKERS = 4

def create_corpus():
    sentences = list(map(remove_stopwords_id, open(FILE_DIR).read().splitlines()))
    corpus = list(map(simple_preprocess, sentences))
    print(corpus[:2], "\nSentences: -->", len(corpus))
    uniqset = set(word for l in corpus for word in l) 
    print(len(uniqset), "Unique Terms")
    return(corpus)

def create_word2vec(save=True):
    corpus = create_corpus()
    model = Word2Vec(
        corpus, 
        size=SIZE, 
        window=WINDOW, 
        min_count=5,
        workers=WORKERS,
        iter=ITER)
    if save:
        model.save(MODEL_DIR)
        print("Model Saved:", MODEL_DIR)

    return(model)

# print(model.wv.most_similar("kartu"))
# [('kredit', 0.5386360287666321), 
# ('berbagai', 0.5347478985786438), 
# ('sejalan', 0.502410888671875), 
# ('tahapan', 0.49144789576530457), 
# ('menerapkan', 0.41903647780418396), 
# ('terkemuka', 0.3761982023715973), 
# ('tahun', 0.3546695113182068), 
# ('atm', 0.3403625190258026), 
# ('nama', 0.2962668836116791)]


if __name__ == '__main__':
    model = create_word2vec()

# model.corpus_total_words -> 139
# model.wv['bca'] # ndarray of length 10
# model.wv.vocab['atm'].count -> 5
