# Education Toolkit for Bahasa Indonesia NLP
[![PyPI version](https://img.shields.io/pypi/v/elang?color=green)](https://badge.fury.io/py/elang) [![PyPI license](https://img.shields.io/pypi/l/Elang?color=red)](https://pypi.python.org/pypi/elang/) [![Activity](https://img.shields.io/github/commit-activity/m/onlyphantom/elang)](https://github.com/onlyphantom/elang) [![maintained](https://img.shields.io/maintenance/yes/2020)](https://github.com/onlyphantom/elang/graphs/commit-activity) [![PyPI format](https://img.shields.io/pypi/format/elang)](https://pypi.org/project/elang/https://pypi.org/project/elang/) [![pypi downloads](https://img.shields.io/pypi/dm/elang)](https://pypi.org/project/elang/https://pypi.org/project/elang/)

> This repository is the PyPI version intended for production use. It is maintained for accuracy purposes. For example code, experimental / in-development features and tutorial materials, use [Elangdev](https://github.com/onlyphantom/elangdev) instead. 

Elang is an acronym that combines the phrases **Education (E)** and **Language Understanding (Lang)**. It is an education-centric toolkit to demonstrate the ideas behind many Natural Language Processing strategies commercially used today. 

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