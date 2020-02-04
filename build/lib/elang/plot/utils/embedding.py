import sys, os.path
import gensim
from gensim.models import Word2Vec

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def plot2d_demo(model, words=None):
    assert (
        model.vector_size >= 2
    ), "This function expects a model of size 2 (2-dimension word vectors) or higher."

    if words is None:
        words = [words for words in model.wv.vocab]

    word_vec = np.array([model.wv[word] for word in words])

    if model.vector_size > 2:
        pca = PCA(2)
        word_vec = pca.fit_transform(word_vec)

    with plt.style.context("seaborn-pastel"):
        plt.figure(figsize=(7, 5), dpi=180)
        plt.scatter(word_vec[:, 0], word_vec[:, 1], s=5, edgecolors="k", c="c")

        for word, (x, y) in zip(words, word_vec):
            plt.text(x - 0.02, y + 0.02, word, fontsize=5)

    plt.show()


if __name__ == "__main__":
    MODEL_PATH = (
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        + "/word2vec/model/demo2d.model"
        # + "/word2vec/model/demo500d.model"
    )
    model = Word2Vec.load(MODEL_PATH)
    print("Loaded from Path:", MODEL_PATH, "\n", model)

    # plot2d_demo(model, words=["bca", "mandiri", "uob", "algoritma", "airbnb"])
    plot2d_demo(model)
