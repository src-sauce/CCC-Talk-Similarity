"""
modelTraining.py
"""


import json
import numpy as np
from gensim.corpora import Dictionary
from gensim.models import LdaModel
from pprint import pprint
from sklearn.model_selection import train_test_split
from DownloadData.download import SRTs
from Similarity.parsing import getTextsByLang, _chars, _tokenise, getStopwords, getStopwordsByLang


def training():
    """  """

    configs = json.load(open('config.json', 'r'))

    srt_api = SRTs(configs, _nd=0)

    language = configs['LANG']
    print("Chosen language '%s'" % language)
    language_texts = getTextsByLang(texts=srt_api.raw_texts.values(), lang=language)

    texts = language_texts[language]
    print("Available languages '%s'" % [lang for lang in language_texts.keys()])
    print("Documents per language '%s'" % [len(language_texts[lang]) for lang in language_texts.keys()])


    texts = np.array(language_texts[language])
    print("Using '%s' documents to proceed" %len(texts))


    train_list, test_list = train_test_split(texts, test_size=0.25)
    train_list = _chars(train_list)
    print(train_list[0])

    # stopword_path = configs["NLP"]["File"]
    stopwords = getStopwordsByLang(language=language)
    print('Stopwords', stopwords[:15])

    if configs["NLP"]["Stops"]:
        words = _tokenise(np.unique(train_list), stopwords)
    else:
        words = _tokenise(np.unique(train_list))

    dictionary = Dictionary(words)
    dictionary.filter_extremes()
    print(dictionary)

    corpus = [dictionary.doc2bow(text.split(' ')) for text in train_list]

    # TODO Dive deeper into topic modelling and tune some parameters
    lda = LdaModel(
        num_topics = 25, # Number of feature distributions (topics) searched
        corpus = corpus,
        id2word = dictionary,
        distributed = False,
        chunksize = 2000, # Number of docs analysed in one epoch
        passes = 1,
        update_every = 1,

        alpha = 'symmetric', # shape of alpha distribution (dist of topics)
        eta = None,
        decay = 0.5,
        offset = 1.0,
        eval_every = 10,

        iterations = 50, # Number of iterations
        gamma_threshold = 0.001, # Threshold for gamma distribution (topics)
        minimum_probability = 0.01, # No topics below this probability

        random_state = None,
        ns_conf = None,
        per_word_topics = False, # Additionally computes a list of topics for each word in the corpus
        minimum_phi_value = 0.01
    )

    pprint(lda.show_topics(num_topics=10, num_words=10, log=False, formatted=False))

    save_paths = [configs["DICT"], configs["MODEL"]]
    dictionary.save_as_text(save_paths[0])
    lda.save(save_paths[1])

    print("Bye! =)")


if __name__ == "__main__":
    training()

