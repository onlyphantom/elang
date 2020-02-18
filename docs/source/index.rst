Elang Documentation & Quick Start
===================================

The 5-min Guide to Word Embeddings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you have a `Word2Vec` model and would like to generate a 2-dimensional word embedding visualization, this can be done through the `plot2d` function: 

.. code-block:: python
   :emphasize-lines: 4

   from elang.plot.utils import plot2d
   from gensim.models import Word2Vec  
   model = Word2Vec.load("path.to.model")
   plot2d(model)

The default method for dimensionality reduction (to obtain exactly two dimensions) is Principal Component Analysis (PCA). This, and the other parameters can be specified as optional parameters. 

For example, you may not wish to plot all the words in your Word2Vec model, and only wish to see a list of words. This can be done using the `words` parameter; 
You may optionally wish to bring attention to a small subset of words within the plot, and this can be done using the `targets` parameter. 

.. code-block:: python

   from elang.plot.utils import plot2d
   list_of_words_to_appear = ["bca", "mandiri", "uob", "algoritma", "airbnb", ..., "emiten"]
   plot2d(model, 
      # method for dimensionality reduction
      method="TSNE",
      # only show following words in the final plot  
      words=list_of_words_to_appear,
      # target words are given special emphasis in the final plot
      targets=['uob', 'mandiri','bca']
   )

.. image:: assets/pca.png
   :width: 300
   :alt: Word Embeddings using Elang

.. toctree::
   :maxdepth: 2
   :caption: Contents:

The 5-min Guide to NLP Preprocessing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Elang comes with a number of pre-processing functions to make cleaning data in Bahasa Indonesia a little easier. 

The `remove_*` group of functions parses a string and eliminate any occurrences of words in a pre-determined list (negative list).

.. code-block:: python

   from elang.word2vec.utils import *
   x = "Oh ya, saya sudah pernah ke Hutan Ingatan Pasar Seni, Bandung, Senin 25 Maret kemarin. Tempat ini bagus anjir."
   x = remove_stopwords_id(x)
   # x: "Saya pernah ke Hutan Ingatan Pasar Seni, Bandung, Senin 25 Maret kemarin. Tempat bagus anjir."

   x = remove_region_id(x)
   # x: "Saya pernah ke Hutan Ingatan Pasar Seni, Senin 25 Maret kemarin. Tempat bagus anjir."
   
   x = remove_calendar_id("Hutan Ingatan Pasar Seni, Bandung, Senin 25 Maret")
   # x: "Saya pernah ke Hutan Ingatan Pasar Seni kemarin. Tempat bagus anjir."

   x = remove_vulgarity_id(x)
   # x: "Saya pernah ke Hutan Ingatan Pasar Seni kemarin. Tempat bagus."



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
