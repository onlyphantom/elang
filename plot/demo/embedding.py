import sys, os.path
import gensim
from gensim.models import Word2Vec

import numpy as np
import matplotlib.pyplot as plt


def hash(astring):
    return ord(astring[0])


MODEL_PATH = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    + "/word2vec/model/demo.model"
)

model = Word2Vec.load(MODEL_PATH)
print("Loaded from Path:", MODEL_PATH, "\n", model)


def plot2d_demo(model, words=None):
    # TODO: if model is above 2 dimension do dimensionality reduction?
    assert (
        model.vector_size == 2
    ), "This function expects a model of exactly size 2 (2-dimension word vectors)."

    if words is None:
        words = [words for words in model.wv.vocab]
        print(words)

    word_vec = np.array([model.wv[word] for word in words])
    with plt.style.context("dark_background"):
        plt.figure(figsize=(7, 5), dpi=180, frameon=False)
        plt.scatter(word_vec[:, 0], word_vec[:, 1], s=5, edgecolors="k", c="c")

        for word, (x, y) in zip(words, word_vec):
            plt.text(x - 0.02, y + 0.02, word, fontsize=5)

    plt.show()


# plot2d_demo(model, words=["bca", "mandiri", "uob", "algoritma", "airbnb"])
plot2d_demo(model)
