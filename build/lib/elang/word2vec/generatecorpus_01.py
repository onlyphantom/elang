import os
from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
from utils import remove_stopwords_id

SIZE = 2
REAL_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_DIR = REAL_PATH + "/simple_preprocess/demosentences.txt"
MODEL_DIR = REAL_PATH + f"/model/demo{SIZE}d.model"
WINDOW = 2
ITER = 1000
WORKERS = 4


def create_corpus():
    sentences = list(map(remove_stopwords_id, open(FILE_DIR).read().splitlines()))
    corpus = list(map(simple_preprocess, sentences))
    print(corpus[7])
    print("Sentences: -->", len(corpus))
    uniqset = set(word for l in corpus for word in l)
    print("Unique Terms -->", len(uniqset))
    print(uniqset)
    return corpus


def hash(astring):
    return ord(astring[0])


def create_word2vec(save=False):
    corpus = create_corpus()
    model = Word2Vec(
        corpus,
        size=SIZE,
        window=WINDOW,
        min_count=1,
        workers=WORKERS,
        iter=ITER,
        seed=3,
        hashfxn=hash,
    )
    if save:
        model.save(MODEL_DIR)
        print("Model Saved:", MODEL_DIR)

    return model


if __name__ == "__main__":
    model = create_word2vec(save=False)


# Try: kartu, rekening
print(model.wv.most_similar("bca"), "\n", "----")
print(model.wv.doesnt_match("mandiri agustus uob bca".split()), "\n", "----")
print(model.wv.doesnt_match("kartu airbnb kredit debit".split()), "\n", "----")
print(
    model.wv.doesnt_match("perusahaan sekretaris karyawan dekade".split()), "\n", "----"
)

