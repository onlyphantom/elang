# Education Toolkit for Bahasa Indonesia NLP
[![PyPI version](https://img.shields.io/pypi/v/elang?color=green)](https://badge.fury.io/py/elang) [![PyPI license](https://img.shields.io/pypi/l/Elang?color=red)](https://pypi.python.org/pypi/elang/) [![Activity](https://img.shields.io/github/commit-activity/m/onlyphantom/elang)](https://github.com/onlyphantom/elang) [![maintained](https://img.shields.io/maintenance/yes/2020)](https://github.com/onlyphantom/elang/graphs/commit-activity) [![PyPI format](https://img.shields.io/pypi/format/elang)](https://pypi.org/project/elang/) [![pypi downloads](https://img.shields.io/pypi/dm/elang)](https://pypi.org/project/elang/) [![Documentation Status](https://readthedocs.org/projects/elang/badge/?version=latest)](https://elang.readthedocs.io/en/latest/?badge=latest)


Elang is an acronym that combines the phrases **Education (E)** and **Language Understanding (Lang)**. It is an education-centric toolkit to demonstrate the ideas behind many Natural Language Processing strategies commercially used today, including word embeddings and pre-trained Bahasa Indonesia models for transfer learning. [Quick Start and Documentation](https://elang.readthedocs.io/en/latest/) helps you get started in 5 minutes.

<img align="left" width="35%" src="https://github.com/onlyphantom/elangdev/blob/master/assets/elang_light.png?raw=true" style="margin-right:10%">

## Elang
Elang also means "eagle" in Bahasa Indonesia, and the _elang Jawa_ (Javan hawk-eagle) is the national bird of Indonesia, more commonly referred to as Garuda. 

The package provides a collection of utility functions and tools that interface with `gensim` and `scikit-learn`, as well as curated negative lists for Bahasa Indonesia (kata kasar / vulgar words, _stopwords_ etc) and useful preprocesisng functions.

# Quick Demo

Install `elang`:
```bash
pip install elang
```

Performing word embeddings in **4 lines of code** gets you a visualization:
```py
from elang.plot.utils import plot2d
from gensim.models import Word2Vec

model = Word2Vec.load("path.to.model")
plot2d(model)
# output:
```

<img width="50%" src="https://github.com/onlyphantom/elangdev/raw/master/assets/embedding.png">

It even looks like a soaring eagle with its outstretched wings!

### Scikit-Learn Compatability
Because the dimensionality reduction procedure is handled by the underlying `sklearn` code, you can use any of the valid [parameters](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) in the function call and they will be handed off to the underlying method. Common examples are the `perplexity`, `n_iter` and `random_state` parameters:

```py
model = Word2Vec.load("path.to.model")
bca = model.wv.most_similar("bca", topn=14)
similar_bca = [w[0] for w in bca]
plot2d(
    model,
    method="TSNE",
    targets=similar_bca,
    perplexity=20,
    early_exaggeration=50,
    n_iter=2000,
    random_state=0,
)
```

Output:

<img width="50%" src="https://github.com/onlyphantom/elangdev/raw/master/assets/tsne.png">