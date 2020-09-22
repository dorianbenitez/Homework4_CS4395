#######
# File: Homework4_p2_drb160130.py
# Author: Dorian Benitez (drb160130)
# Date: 9/20/2020
# Purpose: CS 4395.001 - Homework #4 (Language Models, Program 2)
#######

import pickle
from nltk import word_tokenize, ngrams


# This function will calculate the probability of each language used per line
def compute_prob(line, unigram, bigram, V):
    p_laplace = 1
    unigrams_tokens = word_tokenize(line)
    bigrams_list = list(ngrams(unigrams_tokens, 2))

    for b in bigrams_list:
        n = bigram[b] if b in bigram else 0
        d = unigram[b[0]] if b[0] in unigram else 0
        p_laplace = p_laplace * ((n + 1) / (d + V))

    return p_laplace


# Main function
if __name__ == '__main__':

    # Read the pickled dictionaries created in program 1
    english_unigram = pickle.load(open('english_unigram', 'rb'))
    english_bigram = pickle.load(open('english_bigram', 'rb'))

    french_unigram = pickle.load(open('french_unigram', 'rb'))
    french_bigram = pickle.load(open('french_bigram', 'rb'))

    italian_unigram = pickle.load(open('italian_unigram', 'rb'))
    italian_bigram = pickle.load(open('italian_bigram', 'rb'))

    # Get the total length of all three unigrams
    V = len(english_unigram) + len(french_unigram) + len(italian_unigram)

    # Open the test file and append each line to a list
    with open('LangId.test', 'r') as f:
        test_file = f.readlines()
    f.close()

    # Open the actual solution and append each each line to a list
    with open('LangId.sol', 'r') as f:
        actual_solution = f.readlines()
    f.close()

    # Create/Write a new file to store our predicted solution
    f = open("PredictedSolutionFile.txt", "w")
    f.close()

    # These values are to be used later in the program
    predicted_solution = []
    wrong_lines = []
    correct_count = 0
    line_number = 0

    # For each test file, calculate the probability for each language and write the
    # language with the highest probability to a file.
    for line in test_file:
        line_number += 1

        english_prob = compute_prob(line, english_unigram, english_bigram, V)
        french_prob = compute_prob(line, french_unigram, french_bigram, V)
        italian_prob = compute_prob(line, italian_unigram, italian_bigram, V)

        # Write the language with the highest probability to the "PredictedSolutionFile.txt" file
        if english_prob > french_prob and english_prob > italian_prob:
            with open('PredictedSolutionFile.txt', 'a') as f:
                f.write(str(line_number) + " English\n")
            f.close()

        elif french_prob > english_prob and french_prob > italian_prob:
            with open('PredictedSolutionFile.txt', 'a') as f:
                f.write(str(line_number) + " French\n")
            f.close()

        else:
            with open('PredictedSolutionFile.txt', 'a') as f:
                f.write(str(line_number) + " Italian\n")
            f.close()

    # Open the predicted solution file and append each line to a list
    with open('PredictedSolutionFile.txt', 'r') as f:
        predicted_solution = f.readlines()
    f.close()

    # This compares the actual solution to our predicted solution
    for i in range(len(predicted_solution)):
        if predicted_solution[i] == actual_solution[i]:
            correct_count += 1
        else:
            wrong_lines.append(i + 1)

    # Calculate and print number of correct lines, total number of lines,
    # the predicted accuracy, and the lines that were categorized incorrectly
    accuracy = correct_count / len(predicted_solution)
    print("Number of correct lines:", correct_count)
    print("Total lines:", len(predicted_solution))
    print("Accuracy:", '%.2f' % accuracy)
    print("Incorrect lines:", wrong_lines)
