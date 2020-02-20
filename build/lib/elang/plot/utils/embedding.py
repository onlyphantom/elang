import sys, os.path
import gensim
from gensim.models import Word2Vec

import numpy as np
import matplotlib.pyplot as plt


def plot2d(model, words=None, method="PCA", targets=[], *args, **kwargs):
    """plot2d Plot word embeddings in 2-dimension
    
    Create a Matplotlib plot to display word embeddings in 2 dimensions, using a specified dimensionality reduction technique if the word vectors have more than 2 dimensions.
    Optionally accepts a `list` for the `words` parameter, to display only a subset of words from the `model`'s dictionary. 
    Optionally accepts a `list` for the `targets` parameter, to emphasize in bold fontface a subset of words
    
    Any other parameters specified using the `*args` or `**kwargs` is unpacked and passed on to the underlying dimensionality reduction method in `sklearn`.

    :param model: An instance of Word2Vec
    :type model: Word2Vec
    :param words: List of words to render in plot -- when None all words in the `model` are plotted, defaults to None
    :type words: list or None, optional
    :param method: Method for dimensionality reduction, defaults to "PCA"
    :type method: str, optional
    :param targets: List of words to be emphasized using a bold font in the plot, defaults to []
    :type targets: list, optional
    :return: A matplotlib figure
    :raises AssertionError: Ensure `model` is size 2 (2-dimension word vectors) (2-dimension word vectors) or higher
    """
    assert (
        model.vector_size >= 2
    ), "This function expects a model of size 2 (2-dimension word vectors) or higher."

    if isinstance(targets, str):
        try:
            targets = [targets]
        except TypeError:
            raise TypeError("The targets parameter expect a python list")

    if words is None:
        words = [word for word in model.wv.vocab]
    else:
        try:
            words = [word for word in words if word in model.wv.vocab]
        except TypeError as e:
            raise TypeError("The 'words' parameter expect a python list")

    word_vec = np.array([model.wv[word] for word in words])
    try:
        if model.vector_size > 2:
            if method == "PCA":
                from sklearn.decomposition import PCA

                word_vec = PCA(2, *args, **kwargs).fit_transform(word_vec)

            elif method == "TSNE":
                from sklearn.manifold import TSNE

                word_vec = TSNE(2, *args, **kwargs).fit_transform(word_vec)

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
    except ValueError as e:
        raise ValueError("Fail to perform dimensionality reduction.")
