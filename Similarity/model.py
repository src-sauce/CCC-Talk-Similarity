"""
modelTraining.py
"""


import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from gensim.corpora import Dictionary
from gensim.models import LdaModel
from pprint import pprint
from sklearn.model_selection import train_test_split

from DownloadData.download import SRTs
from Similarity.parsing import getTextsByLang, _chars, _tokenise, getStopwords, getStopwordsByLang


def main(train=False):
    """  """

    configs = json.load(open('config.json', 'r'))

    srt_api = SRTs(configs, _nd=0)

    file_names = list(srt_api.raw_texts.keys())

    language = configs['LANG']
    print("Chosen language '%s'" % language)
    language_texts, lang_indexes = getTextsByLang(texts=srt_api.raw_texts.values(), lang=language)

    texts = language_texts[language]
    print("Available languages '%s'" % [lang for lang in language_texts.keys()])
    print("Documents per language '%s'" % [len(language_texts[lang]) for lang in language_texts.keys()])

    texts = np.array(language_texts[language])
    # keep file names synchronized with chosen lang
    file_names = [file_names[index] for index in lang_indexes[language]]
    print("Using '%s' documents to proceed" %len(texts))

    texts = _chars(texts)
    print(texts[0])

    # stopword_path = configs["NLP"]["File"]
    stopwords = getStopwordsByLang(language=language)
    print('Stopwords', stopwords[:15])

    if configs["NLP"]["Stops"]:
        words = _tokenise(np.unique(texts), stopwords)
    else:
        words = _tokenise(np.unique(texts))

    dictionary = Dictionary(words)
    dictionary.filter_extremes()
    print(dictionary)

    corpus = [dictionary.doc2bow(text.split(' ')) for text in texts]

    # Split train and test
    X_train, X_test, train_names, test_names = train_test_split(corpus, file_names, test_size=0.25)
    print(len(X_train), len(X_test))
    print(test_names)

    if train:
        # TODO Dive deeper into topic modelling and tune some parameters
        lda = LdaModel(
            num_topics = num_topics, # Number of feature distributions (topics) searched
            corpus = X_train,
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

    else:
        save_paths = [configs["DICT"], configs["MODEL"]]
        dictionary = Dictionary.load_from_text(save_paths[0])
        lda = LdaModel.load(save_paths[1])
        pprint(lda.show_topics(num_topics=10, num_words=10, log=False, formatted=False))

        # Sparse Topic encode
        X_test_topics = []
        for bow_doc in X_test:
            encoded_topics = np.zeros(shape=lda.num_topics)
            for topic in lda.get_document_topics(bow=bow_doc):
                topic_num = topic[0]
                topic_prob = topic[1]
                encoded_topics[topic_num] += topic_prob
            X_test_topics.append(encoded_topics)

        pprint(X_test_topics)

        # for plotting get small names
        plot_names = [name.split('-')[-1] for name in test_names]

        from scipy.spatial.distance import cosine
        similarities = []
        # Measure all sims
        for encoded_topic in X_test_topics:
            similarities.append(
                [1 - cosine(encoded_topic, encoded_topic2) # similarity = 1 - distance
                 for encoded_topic2 in X_test_topics]
                )
        sim_df = pd.DataFrame(data=similarities, columns=plot_names, index=plot_names)
        print(sim_df)

        # Seaborns heatmap does not support long label names
        # sns.heatmap(sim_df, xticklabels=False, yticklabels=False, annot=False)
        plt.imshow(sim_df.values)
        plt.show()
        pprint(sim_df.index.values)

    print("Bye! =)")



if __name__ == "__main__":
    main(train=False)

