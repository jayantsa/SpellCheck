from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
import re
from collections import Counter
glove_input_file = 'glove.6B.100d.txt'
glove_output_file = 'glove.6B.100d.txt.word2vec'
glove2word2vec(glove_input_file, glove_output_file)


# load the Stanford GloVe model
filename = 'glove.6B.100d.txt.word2vec'
model = KeyedVectors.load_word2vec_format(filename, binary=False)
words = model.index2word
w_rank = {}

for i,word in enumerate(words):
    w_rank[word] = i

WORDS = w_rank


def P(word): 
    "Top most word "
    return - WORDS.get(word,0)

def correction(word): 
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))