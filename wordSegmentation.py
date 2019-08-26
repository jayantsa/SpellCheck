import os
#importing symspell module
from symspellpy.symspellpy import SymSpell,Verbosity

#loading a frequency dictionary
# if max edit distance==0, Only Word segments will be generated without spell correction
max_edit_distance_dictionary_word_Segmentation = 1


prefix_length = 7

sym_spell_wordSegmentation = SymSpell(max_edit_distance_dictionary_word_Segmentation, prefix_length)
dictionary_path = os.path.join(os.path.dirname(__file__),
                               "frequency_dictionary_en_82_765.txt")
term_index = 0 
count_index = 1
if not sym_spell_wordSegmentation.load_dictionary(dictionary_path, term_index, count_index):
    print("Dictionary file not found")


def wordSegmentation(input_term):
    
    result = sym_spell_wordSegmentation.word_segmentation(input_term)
    return result.corrected_string.split()
