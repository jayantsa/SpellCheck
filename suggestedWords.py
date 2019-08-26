import os

from symspellpy.symspellpy import SymSpell, Verbosity  # import the module

max_edit_distance_dictionary = 2
prefix_length = 7
# create object
sym_spell = SymSpell(max_edit_distance_dictionary, prefix_length)
# load dictionary
dictionary_path = os.path.join(os.path.dirname(__file__),
                               "frequency_dictionary_en_82_765.txt")
term_index = 0  # column of the term in the dictionary text file
count_index = 1  # column of the term frequency in the dictionary text file
if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
    print("Dictionary file not found")


def correctedWords(input_term,verbosity_type):
    max_edit_distance_lookup = 2
    suggestion_verbosity = Verbosity.ALL
    if verbosity_type==1:
        suggestion_verbosity = Verbosity.TOP
    elif verbosity_type==2:
        suggestion_verbosity = Verbosity.CLOSEST

    suggestions = sym_spell.lookup(input_term, suggestion_verbosity,
                                   max_edit_distance_lookup)
    # display suggestion term, term frequency, and edit distance
    output = []
    for suggestion in suggestions:
        output.append(suggestion.term)
    return output

