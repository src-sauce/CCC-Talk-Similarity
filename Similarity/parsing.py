

import re
import os
import nltk.corpus
from guess_language import guess_language


__author__ = "armin@dotarmin.info"


# Following base regex of https://github.com/alexalemi/
# https://github.com/alexalemi/segmentation/blob/master/code/segmentart.py
hyphenline = re.compile(r"-\s*\n\s*")
punctuations = re.compile(r"""(["#$%&\'()*+,-./:;<=>@[\\\]^_`{|}~])""")
punct_replace = re.compile(r"([\?!])")
nonlet = re.compile(r"([^A-Za-z0-9äöüÄÖÜß. ])")
multiwhite_pat = re.compile(r"\s+")


words = set(nltk.corpus.words.words('en'))


def apply_regex(text):
    text = hyphenline.sub("", text)
    text = punct_replace.sub(r".", text)
    text = punctuations.sub(r" \1 ", text)
    text = nonlet.sub(r" \1 ", text)
    text = nonlet.sub(r"", text)
    text = multiwhite_pat.sub(r" ", text)
    text = text.strip()
    # print('Doc after regex = %s...'% text[:50])
    return text


def _chars(documents):
    return [apply_regex(doc) for doc in documents]


def _tokenise(documents, stopwords=None, min_length=3):
    # TODO: Add 'min_freq' parameter and filter words below this parameter
    # TODO: based on word frequency computed on each document
    # TODO: based on word frequency computed on all documents
    if stopwords is None:
        result = [[word.lower()
                 for word in document.split()
                 if word.lower() in words and len(word) >= min_length]
                for document in documents]
    else:
        result = [[word.lower()
                 for word in document.split()
                 if word.lower() not in stopwords and word.lower() in words and len(word) >= min_length]
                for document in documents]
    return result


def getTextsByLang(texts, lang):
    language_texts = {}
    for text in texts:
        language = guess_language(text)
        if language in language_texts.keys():
            language_texts[language].append(text)
        else:
            language_texts[language] = [text]
    return language_texts


def getStopwordsByLang(language=None):
    # TODO define json structure for short langauge to nltk-language mapping!
    stopwords = []
    if language == "en":
        stopwords = nltk.corpus.stopwords.words('english')
    elif language == "ger":
        stopwords = nltk.corpus.stopwords.words('german')
        stopwords.extend(nltk.corpus.stopwords.words('english'))
    else:
        # Default stopword list to english
        stopwords = nltk.corpus.stopwords.words('english')
    return stopwords


def getStopwords(path):
    stop_words = []
    for line in open(path, 'r').readlines():
        if ';' not in line:
            stop_words.append(hyphenline.sub('', line).strip())
    en = set(nltk.corpus.stopwords.words('english'))
    stop_words.extend(en)
    return [w.lower() for w in stop_words]

