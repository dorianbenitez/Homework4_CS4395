#######
# File: Homework4_p1_drb160130.py
# Author: Dorian Benitez (drb160130)
# Date: 9/20/2020
# Purpose: CS 4395.001 - Homework #4 (Language Models, Program 1)
#######

import sys
import re
from nltk import word_tokenize
import pickle


# Create a function with a filename as argument
def process_lang(raw_text):
    # Read in the text, remove newlines, and make the text lowercase
    text = re.sub(r'[.?!,:;()\-\'\"\d]', ' ', raw_text.lower())

    # Tokenize the text
    unigrams = word_tokenize(text)

    # Use nltk to create a bigrams list
    bigrams_list = [(unigrams[k], unigrams[k + 1]) for k in range(len(unigrams) - 1)]

    # Create a unigrams list
    unigrams_list = list(unigrams)

    # Use the bigram list to create a bigram dictionary of bigrams and counts
    bigram_dict = {b: bigrams_list.count(b) for b in set(bigrams_list)}

    # Use the unigram list to create a unigram dictionary of unigrams and counts
    unigram_dict = {t: unigrams_list.count(t) for t in set(unigrams_list)}

    # Return the unigram dictionary and bigram dictionary from the function
    return unigram_dict, bigram_dict


# Main function
if __name__ == '__main__':

    # Read each of the three files and store them as raw text
    with open('LangId.train.English', 'r') as f:
        english_raw = f.read()
    f.close()
    with open('LangId.train.French', encoding="utf8") as f:
        french_raw = f.read()
    f.close()
    with open('LangId.train.Italian', encoding="utf8") as f:
        italian_raw = f.read()
    f.close()

    # This block will call the processing function for the english training file
    # and pickle the english unigram and bigram dictionaries
    english_unigram, english_bigram = process_lang(english_raw)
    pickle.dump(english_unigram, open('english_unigram', 'wb'))
    pickle.dump(english_bigram, open('english_bigram', 'wb'))

    # This block will call the processing function for the french training file
    # and pickle the french unigram and bigram dictionaries
    french_unigram, french_bigram = process_lang(french_raw)
    pickle.dump(french_unigram, open('french_unigram', 'wb'))
    pickle.dump(french_bigram, open('french_bigram', 'wb'))

    # This block will call the processing function for the italian training file
    # and pickle the italian unigram and bigram dictionaries
    italian_unigram, italian_bigram = process_lang(italian_raw)
    pickle.dump(italian_unigram, open('italian_unigram', 'wb'))
    pickle.dump(italian_bigram, open('italian_bigram', 'wb'))
    print('\nProgram ended')
