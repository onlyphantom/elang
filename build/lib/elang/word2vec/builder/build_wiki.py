import os, re, multiprocessing

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# realpath = os.path.dirname(os.path.realpath(__file__))
folderpath = os.getcwd() + "/corpus"

##### ##### ##### #####
# BUILD FROM WIKIPEDIA
##### ##### ##### #####
def build_from_wikipedia_random(
    n=10, lang="id", save=False, model=True, *args, **kwargs
):
    """build_from_wikipedia_random Builds a corpus from random articles on Wikipedia, optionally training, and returning, a Word2Vec model if `model` is set to True.
    
    Builds a corpus from `n` Wikipedia articles (either English or Indonesian version, defined by `lang`). When `save` is True, the corpus is saved in the `/corpus` directory. When `model` is True, a Word2Vec model is trained on the corpus and returned.

    Any other parameters specified using `*args` or `**kwargs` is unpacked and passed on to the underlying `Word2Vec` method from gensim.

    :param n: The number of random articles to parse, defaults to 10
    :type n: int, optional
    :param lang: The language version of Wikipedia to parse from (`en` for English, `id` for Indonesian), defaults to "id"
    :type lang: str, optional
    :param save: Save the built corpus in the `/corpus` directory, defaults to False
    :type save: bool, optional
    :param model: Train and return a Word2Vec model on the built corpus, defaults to True
    :type model: bool, optional
    :raises ValueError: `Lang` be one of 'id' or 'en'
    :return: A Word2Vec model trained on the built corpus when `model` is True
    :rtype: Word2Vec model
    """
    articles = []

    url_base = f"https://{lang}.wikipedia.org/wiki/"
    if lang.lower() == "id":
        random_url = url_base + "Istimewa:Halaman_sembarang"
    elif lang.lower() == "en":
        random_url = url_base + "Special:Random"
    else:
        raise ValueError("Please supply one of 'id' or 'en' to the lang argument.")

    for page in tqdm(range(n)):
        url = requests.request("GET", random_url).url
        slug = re.sub(url_base, "", url)
        articles.append(_get_wikipedia_article(slug, url_base))

    if save:
        _make_corpus_directory()
        filename = f"wikipedia_random_{n}_{lang}.txt"
        _save_content2txt(articles, filename)

    if model:
        w2vmodel = _model_from_articles(articles, lang=lang, *args, **kwargs)
        return w2vmodel


def build_from_wikipedia_branch(
    slug, levels=2, lang="id", save=False, model=True, *args, **kwargs
):
    """build_from_wikipedia_branch Builds a corpus from articles on Wikipedia, by branching off from a specified topic ("slug"). optionally training, and returning, a Word2Vec model if `model` is set to True.
    
    Builds a corpus from articles on Wikipedia, by branching off from a specified topic ("slug") and finding all related articles, and related articles of those related articles, up to a specified level. When `save` is True, the corpus is saved in the `/corpus` directory. When `model` is True, a Word2Vec model is trained on the corpus and returned.

    Any other parameters specified using `*args` or `**kwargs` is unpacked and passed on to the underlying `Word2Vec` method from gensim.
    
    :param slug: A string that is appended to the final segment of the Wikipedia url path ("slug"), defaults to None
    :type slug: string or None, optional
    :param levels: Determines the level of branching (level 1 refer to all directly related Wikipedia article to the slug, level 2 finds related articles to those related articles in level 1 etc), defaults to 2
    :type levels: int, optional
    :param lang: The language version of Wikipedia to parse from (`en` for English, `id` for Indonesian), defaults to "id"
    :type lang: str, optional
    :param save: Save the built corpus in the `/corpus` directory, defaults to False
    :type save: bool, optional    
    :param model: Train and return a Word2Vec model on the built corpus, defaults to True
    :type model: bool, optional
    :raises Exception: Couldn't find Wikipedia article with the supplied slug.
    :return: A Word2Vec model trained on the built corpus when `model` is True
    :rtype: Word2Vec model
    """
    articles = []
    url_base = f"https://{lang}.wikipedia.org/wiki/"
    try:
        article = _get_wikipedia_article(slug, url_base)
        # articles.append(article)
        related_queries = set(article["related_queries"])
    except:
        raise Exception("Couldn't find Wikipedia article with the supplied slug.")

    all_queries = list(related_queries) + [slug]
    queried = []

    for i in range(int(levels)):
        new_queries = []
        for que in set(all_queries):
            if que not in queried and que != "":
                article = _get_wikipedia_article(que, url_base)
                articles.append(article)
                queried.append(que)
                new_queries.extend(article["related_queries"])
        all_queries = list(set(new_queries))
        print(f"Level {i+1} Queried so far: {queried} \n")

    if save:
        _make_corpus_directory()
        filename = f"wikipedia_branch_{slug}_{levels}.txt"
        _save_content2txt(articles, filename)

    if model:
        w2vmodel = _model_from_articles(articles, lang=lang, *args, **kwargs)
        return w2vmodel


def build_from_wikipedia(
    slug=None, n=10, lang="id", levels=2, save=False, model=True, *args, **kwargs
):
    """build_from_wikipedia Build a Word2Vec model by constructing the corpus from Wikipedia articles, either randomly or by branching off from a specified topic ("slug").
    
    A simple wrapper that delegates to the corresponding, lower-level functions such as `build_from_wikipedia_random` and `build_from_wikipedia_branch` based on the parameters it was called with. 
    These functions, in turn, construct a corpus from Wikipedia, and train a Word2Vec model using said corpus.

    When `save` is True (default False), the corpus is saved in the `/corpus` directory. 
    When `model` is True (default True), a Word2Vec model is trained on the corpus and returned.

    :param slug: A string that is appended to the final segment of the Wikipedia url path ("slug"), defaults to None
    :type slug: string or None, optional
    :param n: The number of random articles to parse, defaults to 10
    :type n: int, optional
    :param lang: The language version of Wikipedia to parse from (`en` for English, `id` for Indonesian), defaults to "id"
    :type lang: str, optional
    :param levels: Determines the level of branching (level 1 refer to all directly related Wikipedia article to the slug, level 2 finds related articles to those related articles in level 1 etc), defaults to 2
    :type levels: int, optional
    :param save: Save the built corpus in the `/corpus` directory, defaults to False
    :type save: bool, optional
    :param model: Train and return a Word2Vec model on the built corpus, defaults to True
    :type model: bool, optional
    :return: A Word2Vec model trained on the built corpus when `model` is True
    :rtype: Word2Vec model
    """
    if slug is None:
        return build_from_wikipedia_random(
            lang=lang, n=n, save=save, model=model, *args, **kwargs
        )
    else:
        return build_from_wikipedia_branch(
            slug=slug,
            lang=lang,
            levels=levels,
            save=save,
            model=model,
            *args,
            **kwargs,
        )


##### ##### ##### #####
# INTERNAL HELPER FUNCS
##### ##### ##### #####
def _make_corpus_directory():
    path = folderpath + "/txt"
    if not os.path.exists(path):
        os.makedirs(path)


def _get_wikipedia_article(slug, url_base):
    url_query = url_base + str(slug)
    req = requests.get(url_query)
    soup = BeautifulSoup(req.content, "html.parser")

    article = {}
    article["title"] = soup.find("h1", attrs={"class": "firstHeading"}).text
    article["url"] = url_query

    find_div = soup.find("div", attrs={"class": "mw-parser-output"})
    if find_div is None:
        return
    for s in find_div(["script", "style", "table", "div"]):
        s.decompose()

    find_content = find_div.findAll(
        ["p", "li", "h2.span.mw-headline", "h3.span.mw-headline"]
    )

    article["content"] = " ".join(
        [re.sub(r"\s+", " ", row.text) for row in find_content]
    )

    find_redirect_link = find_div.findAll("a", attrs={"class": "mw-redirect"})
    article["related_queries"] = [link["href"][6:] for link in find_redirect_link]
    return article


def _save_content2txt(dictionary, filename):
    content_list = [d["content"] for d in dictionary if "content" in d.keys()]
    with open(f"{folderpath}/txt/{filename}", "w", encoding="utf-8") as f:
        f.write("\n".join(content_list))
    print("Article content successfully saved to", filename)


def _create_word2vec(corpus, lang, size=100, window=5, iteration=10, min_count=1):
    model = Word2Vec(
        corpus,
        size=size,
        window=window,
        min_count=min_count,
        workers=multiprocessing.cpu_count(),
        iter=iteration,
    )
    
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)

    model.save(f"{folderpath}/{lang}_{size}d.model")

    return model


def _model_from_articles(articles, lang, *args, **kwargs):
    content_list = [d["content"] for d in articles if "content" in d.keys()]
    # corpus = ' '.join(content_list)
    corpus = list(map(simple_preprocess, content_list))
    w2vmodel = _create_word2vec(corpus, lang=lang, *args, **kwargs)
    return w2vmodel
