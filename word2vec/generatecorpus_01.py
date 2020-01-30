import os
from gensim.models import Word2Vec
from simple_preprocess.bcapara import single_para, multi_senc

SIZE= 100
WINDOW = 5
ITER = 10
WORKERS = 4

# build vocabulary and train model on one paragraph
# corpus = single_para()
corpus = multi_senc()
model = Word2Vec(
    corpus, 
    size=SIZE, 
    window=WINDOW, 
    min_count=5,
    workers=WORKERS,
    iter=ITER)

print(model.wv.most_similar("kartu"))
# [('kredit', 0.5386360287666321), 
# ('berbagai', 0.5347478985786438), 
# ('sejalan', 0.502410888671875), 
# ('tahapan', 0.49144789576530457), 
# ('menerapkan', 0.41903647780418396), 
# ('terkemuka', 0.3761982023715973), 
# ('tahun', 0.3546695113182068), 
# ('atm', 0.3403625190258026), 
# ('nama', 0.2962668836116791)]

save_dir = os.path.dirname(os.path.realpath(__file__)) + '/model/fin.model'
print(save_dir)
model.save(save_dir)

# model.corpus_total_words -> 139
# model.wv['bca'] # ndarray of length 10
# model.wv.vocab['atm'].count -> 5
