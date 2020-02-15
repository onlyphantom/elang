import sys, os.path
import gensim
from gensim.models import Word2Vec

import numpy as np
import matplotlib.pyplot as plt


def plot2d(model, words=None, method="PCA", targets=[]):
    assert (
        model.vector_size >= 2
    ), "This function expects a model of size 2 (2-dimension word vectors) or higher."

    assert isinstance(targets, list), "The targets parameter expect a python list"

    if words is None:
        words = [words for words in model.wv.vocab]

    word_vec = np.array([model.wv[word] for word in words])

    if model.vector_size > 2:
        if method == "PCA":
            from sklearn.decomposition import PCA

            word_vec = PCA(2).fit_transform(word_vec)

        elif method == "TSNE":
            from sklearn.manifold import TSNE

            word_vec = TSNE(2).fit_transform(word_vec)

        else:
            raise AssertionError(
                "Model must be one of PCA or TSNE for model with greater than 2 dimensions"
            )

    with plt.style.context("seaborn-pastel"):
        plt.figure(figsize=(7, 5), dpi=180)
        plt.scatter(
            word_vec[:, 0], word_vec[:, 1], s=5, alpha=0.3, edgecolors="k", c="c"
        )

        for word, (x, y) in zip(words, word_vec):
            if word in [elem.lower() for elem in targets if targets]:
                plt.text(x - 0.02, y + 0.02, word, fontsize=5, weight="bold")
            else:
                plt.text(x - 0.02, y + 0.02, word, fontsize=5, alpha=0.5)

    plt.show()
