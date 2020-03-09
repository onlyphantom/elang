import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open('elang/version.py').read())

setuptools.setup(
    name="elang",
    version=__version__,
    author="Samuel Chan, Tomy Tjandra",
    author_email="samuel@algorit.ma",
    description="Word Embedding(E) utilities: Indonesian Language(Lang) Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onlyphantom/elang",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["gensim", "scikit-learn", "matplotlib"],
    keywords="nlp bahasa indonesia indonesian natural language corpus word2vec gensim embedding nltk",
    test_suite="nose.collector",
    tests_require=["nose"],
)
