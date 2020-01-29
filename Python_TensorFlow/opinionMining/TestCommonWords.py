import numpy as np


def generator1(x):

    i = 0

    while i < len(x):
        yield x[i][0],x[i][1]

        i += 1
def generator(x):

    i = 0

    while i < len(x):
        yield x[i]

        i += 1

# train_docs = np.load('train.npy', allow_pickle=True)
test_docs=np.load('test.npy', allow_pickle=True)

tokens = [t for d in test_docs for t in d[0]]

import nltk

text = nltk.Text(tokens, name='NMSC')
  
# selected_words = np.load('selected_words.npy', allow_pickle=True)
selected_words = [a[0] for f in text.vocab().most_common(100) for a in f.split('/')]

print(selected_words)