from math import log
from collections import Counter
import re


def words(text): return re.findall(r'\w+', text.lower())
# cost dictionary 
WORDS = Counter(words(open('big.txt').read()))
wordcost = dict((k, log((i+1)*log(len(WORDS)))) for i,k in enumerate(WORDS))
maxword = max(len(x) for x in WORDS)


def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

print(infer_spaces("unknwords"))
print(infer_spaces("reliublechildrun"))