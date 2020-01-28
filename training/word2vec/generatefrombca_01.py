from gensim.models import Word2Vec
from simple_preprocess.bcapara import corpus_bca

SIZE= 10
WINDOW = 3
ITER = 10
WORKERS = 4
LR = 0.01

# build vocabulary and train model
corpus = corpus_bca()
model = Word2Vec(
    corpus, 
    size=SIZE, 
    window=WINDOW, 
    min_count=1,
    workers=WORKERS,
    iter=ITER)

print(model.wv.most_similar("kartu"))