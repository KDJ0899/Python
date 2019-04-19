'''
Created on 2018. 11. 22.

@author: user
'''
import numpy as np
from konlpy.tag import Okt
import pickle
import nltk


test_docs=np.load('test.npy')

# def read_data(filename):
#     with open(filename, 'rt') as f:
#         data = [line.split('\t') for line in f.read().splitlines()]
#         data = data[1:]   # header 제외
#     return data

def tokenize(doc):
    # norm, stem은 optional
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

def term_exists(doc):
    return {'exists({})'.format(word): (word in set(doc)) for word in selected_words}

selected_words=np.load('selected_words.npy')
# test_data = read_data('ratings_test.txt')

pos_tagger = Okt()

# train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
# test_docs = [(tokenize(row[1]), row[2]) for row in test_data]


test_xy = [(term_exists(d), c) for d, c in test_docs]

f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

print(nltk.classify.accuracy(classifier, test_xy))
# => 0.80418

