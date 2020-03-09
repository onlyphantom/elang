# Word Embedding utilities: Indonesian Language Models
[![PyPI version](https://img.shields.io/pypi/v/elang?color=green)](https://badge.fury.io/py/elang) [![PyPI license](https://img.shields.io/pypi/l/Elang?color=red)](https://pypi.python.org/pypi/elang/) [![Activity](https://img.shields.io/github/commit-activity/m/onlyphantom/elang)](https://github.com/onlyphantom/elang) [![maintained](https://img.shields.io/maintenance/yes/2020)](https://github.com/onlyphantom/elang/graphs/commit-activity) [![PyPI format](https://img.shields.io/pypi/format/elang)](https://pypi.org/project/elang/) [![pypi downloads](https://img.shields.io/pypi/dm/elang)](https://pypi.org/project/elang/) [![Documentation Status](https://readthedocs.org/projects/elang/badge/?version=latest)](https://elang.readthedocs.io/en/latest/?badge=latest)


Elang is an acronym that combines the phrases **Embedding (E)** and **Language (Lang) Models**. Its goal is to help NLP (natural language processing) researchers, Word2Vec practitioners and data scientists be more productive in training language models. By the 0.1 release, the package will include ("marked" checkbox indicates a completed feature):
- Visualizing Word2Vec models
    - [x] 2D plot with emphasis on words of interest
    - [x] 2D plot with neighbors of words
    - _More coming soon_
- Text processing utility
    - [x] Remove stopwords (Indonesian)
    - [x] Remove region entity (Indonesian)
    - [x] Remove calendar words (Indonesian)
    - [x] Remove vulgarity (Indonesian)
- Corpus-building utility
    - [ ] Build Indonesian corpus using wikipedia
    - [ ] Pre-trained models for quick experimentation


<img align="left" width="35%" src="https://github.com/onlyphantom/elangdev/blob/master/assets/elang_light.png?raw=true" style="margin-right:10%">

## Elang
Elang also means "eagle" in Bahasa Indonesia, and the _elang Jawa_ (Javan hawk-eagle) is the national bird of Indonesia, more commonly referred to as Garuda. 

The package provides a collection of utility functions and tools that interface with `gensim`, `matplotlib` and `scikit-learn`, as well as curated negative lists for Bahasa Indonesia (kata kasar / vulgar words, _stopwords_ etc) and useful preprocesisng functions. It abstracts away the mundane task so you can train your Word2Vec model faster, and obtain visual feedback on your model more quickly.

# Quick Demo

### 2-d Word Embedding Visualization
Install the latest version of `elang`:
```bash
pip install --upgrade elang
```

Performing word embeddings in **2 lines of code** gets you a visualization:
```py
from elang.plot.utils import plot2d
from gensim.models import Word2Vec

model = Word2Vec.load("path.to.model")
plot2d(model)
# output:
```

<img width="60%" src="https://github.com/onlyphantom/elangdev/raw/master/assets/embedding.png">

It even looks like a soaring eagle with its outstretched wings!

### Visualizing Neighbors in 2-dimensional space

`elang` also includes visualization methods to help you visualize a user-defined _k_ number of neighbors to each words. When `draggable` is set to `True`, you will obtain a legend that you can move around in the resulting plot.

```py
words = ['bca', 'hitam', 'hutan', 'pisang', 'mobil', "cinta", "pejabat", "android", "kompas"]

plotNeighbours(model, 
    words, 
    method="TSNE", 
    k=15,
    draggable=True)
```

<img width="60%" src="https://github.com/onlyphantom/elangdev/raw/master/assets/neighbors.png">


The plot above plots the 15 nearest neighbors for each word in the supplied `words` argument. It then renders the plot with a draggable legend.

### Scikit-Learn Compatability
Because the dimensionality reduction procedure is handled by the underlying `sklearn` code, you can use any of the valid [parameters](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) in the function call to `plot2d` and `plotNeighbours` and they will be handed off to the underlying method. Common examples are the `perplexity`, `n_iter` and `random_state` parameters:

```py
model = Word2Vec.load("path.to.model")
bca = model.wv.most_similar("bca", topn=14)
similar_bca = [w[0] for w in bca]
plot2d(
    model,
    method="PCA",
    targets=similar_bca,
    perplexity=20,
    early_exaggeration=50,
    n_iter=2000,
    random_state=0,
)
```

Output:

<img width="60%" src="https://github.com/onlyphantom/elangdev/raw/master/assets/tsne.png">