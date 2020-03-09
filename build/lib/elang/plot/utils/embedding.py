import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def plot2d(model, words=None, method="TSNE", targets=[], *args, **kwargs):
    """plot2d Plot word embeddings in 2-dimension
    
    Create a Matplotlib plot to display word embeddings in 2 dimensions, using a specified dimensionality reduction method (`method`) if the word vectors have more than 2 dimensions.
    Optionally accepts a `list` for the `words` parameter, to display only a subset of words from the `model`'s dictionary. When `None`, it will use the first 500 words of the model.  
    Optionally accepts a `list` for the `targets` parameter, to emphasize in bold fontface a subset of words
    
    Any other parameters specified using `*args` or `**kwargs` is unpacked and passed on to the underlying dimensionality reduction method in `sklearn`.

    :param model: An instance of Word2Vec
    :type model: Word2Vec
    :param words: List of words to render in plot -- when None all words in the `model` are plotted, defaults to None
    :type words: list or None, optional
    :param method: Method for dimensionality reduction, defaults to "TSNE"
    :type method: str, optional
    :param targets: List of words to be emphasized using a bold font in the plot, defaults to []
    :type targets: list, optional
    :return: A matplotlib figure
    :raises AssertionError: Ensure `model` is size 2 (2-dimension word vectors) or higher
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
        words = [word for word in list(model.wv.vocab)[1:500]]
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

def plotNeighbours(model, words, k=10, method="TSNE", draggable=False, *args, **kwargs):
    """plotNeighbours Plot and color the `k` nearest neighbors for each word in 2-dimension 

    Create a Matplotlib plot to display word embeddings and their k-nearest neighbors in 2 dimensions, using a specified dimensionality reduction method (`method`) if the word vectors have more than 2 dimensions.
    Set`draggable` to `True` for a draggable legend in the resulting plot. 
    
    Any other parameters specified using `*args` or `**kwargs` is unpacked and passed on to the underlying dimensionality reduction method in `sklearn`.

    :param model: An instance of Word2Vec
    :type model: Word2Vec
    :param words: List of centroid words to render in plot
    :type words: List
    :param k: Number of neighbors for each word, defaults to 10
    :type k: int, optional
    :param method: Method for dimensionality reduction, defaults to "TSNE"
    :type method: str, optional
    :param draggable: Set to `True` if a draggable legend box is preferred, defaults to False
    :type draggable: bool, optional
    :raises AssertionError: Ensure `model` is size 2 (2-dimension word vectors) or higher
    """
    assert (
        model.vector_size >= 2
    ), "This function expects a model of size 2 (2-dimension word vectors) or higher."

    if isinstance(words, str):
        try:
            targets = [targets]
        except TypeError:
            raise TypeError("The targets parameter expect a python list")

    embedding_clusters = []
    word_clusters = [] # (7,10)
    
    try:
        words = [word for word in words if word in model.wv.vocab]
    except TypeError as e:
            raise TypeError("The 'words' parameter expect a python list")

    for word in words:
        neighbors = [] 
        embeddings = []
        for similar, _ in model.wv.most_similar(word, topn=k):
            neighbors.append(similar)
            embeddings.append(model.wv[similar])
        embedding_clusters.append(embeddings)
        word_clusters.append(neighbors)
    embedding_clusters = np.array(embedding_clusters)  
    cent_n, neigh_n, dim_n = embedding_clusters.shape # 7, 10, 50 (centroid, neighborhood, dimensions)
    embedding_clusters = embedding_clusters.reshape(cent_n * neigh_n, dim_n) # (70, 50)
    
    if model.vector_size > 2:
        if method == "PCA":
            from sklearn.decomposition import PCA
            word_vec = PCA(2, *args, **kwargs).fit_transform(embedding_clusters)

        elif method == "TSNE":
            from sklearn.manifold import TSNE
            word_vec = TSNE(2, *args, **kwargs).fit_transform(embedding_clusters)

        else:
            raise AssertionError(
                "Model must be one of PCA or TSNE for model with greater than 2 dimensions"
            )
    else:
        word_vec = embedding_clusters

    word_vec = word_vec.reshape(cent_n, neigh_n, -1) # (7,10,2)
    with plt.style.context("seaborn-pastel"):
        plt.rc('legend', fontsize=7, fancybox=True, framealpha=0.8, facecolor="#777777", edgecolor="#000000")
        plt.rc('font', size=7)
        plt.figure(figsize=(7, 5), dpi=180)
        cmx = cm.get_cmap('Pastel1')
        colors = cmx(np.linspace(0,1,len(words))) # (7,4)
        for word, embedding, neighbor, color in zip(words, word_vec, word_clusters, colors):
            x = embedding[:,0]
            y = embedding[:,1]
            plt.scatter(x, y, color=color, alpha=1, label=word)

            for i, word in enumerate(neighbor):
                plt.annotate(word, alpha=0.6, xy=(x[i], y[i]), size=5)

        if draggable:
            leg = plt.legend()
            leg.set_draggable(state=True)
        else:
            leg = plt.legend(loc="lower left", ncol=min(5, len(words)))
            plt.setp(leg.get_texts(), color='w')
            

    plt.show()
