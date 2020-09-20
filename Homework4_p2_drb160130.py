#######
# File: Homework4_p2_drb160130.py
# Author: Dorian Benitez (drb160130)
# Date: 9/20/2020
# Purpose: CS 4395.001 - Homework #4 (Language Models, Program 2)
#######

import pickle

if __name__ == '__main__':
    # Read the pickled dictionaries created in program 1
    english_unigram = pickle.load(open('english_unigram', 'rb'))
    english_bigram = pickle.load(open('english_bigram', 'rb'))

    french_unigram = pickle.load(open('french_unigram', 'rb'))
    french_bigram = pickle.load(open('french_bigram', 'rb'))

    italian_unigram = pickle.load(open('italian_unigram', 'rb'))
    italian_bigram = pickle.load(open('italian_bigram', 'rb'))

    # Open the test file and append each line to a list
    with open('LangId.test', 'r') as f:
        test_file = f.readlines()
    f.close()

    # Open the actual solution and append each each line to a list
    with open('LangId.sol', 'r') as f:
        real_solution = f.readlines()
    f.close()

    # Create/Write a new file to store our predicted solution
    f = open("PredictedSolutionFile.txt", "w")
    f.close()

    # These values are to be used later in the program
    predicted_solution = []
    wrong_lines = []
    correct_count = 0
    line_number = 0

    # For each test file, calculate a probability for each language and write the
    # language with the highest probability to a file.
    # For each line in the test file, execute this loop
    for line in test_file:
        line_number += 1
        english_count = 0
        french_count = 0
        italian_count = 0

        # For each word in the line, analyze which language (English/French/Italian) is being used
        for word in line.split():
            if word in english_unigram:
                english_count += 1
            elif word in english_bigram:
                english_count += 1
            elif word in french_unigram:
                french_count += 1
            elif word in french_bigram:
                french_count += 1
            elif word in italian_unigram:
                italian_count += 1
            elif word in italian_bigram:
                italian_count += 1

        # Write the language with the highest probability to a list and the "PredictedSolutionFile.txt" file
        if english_count > french_count and english_count > italian_count:
            predicted_solution.append(str(line_number) + " English\n")
            f = open("PredictedSolutionFile.txt", "a")
            f.write(str(line_number) + " English\n")
            f.close()

        elif french_count > english_count and french_count > italian_count:
            predicted_solution.append(str(line_number) + " French\n")
            f = open("PredictedSolutionFile.txt", "a")
            f.write(str(line_number) + " French\n")
            f.close()

        elif italian_count > english_count and italian_count > french_count:
            predicted_solution.append(str(line_number) + " Italian\n")
            f = open("PredictedSolutionFile.txt", "a")
            f.write(str(line_number) + " Italian\n")
            f.close()

        else:
            predicted_solution.append(str(line_number) + " Unknown\n")
            f = open("PredictedSolutionFile.txt", "a")
            f.write(str(line_number) + " Unknown\n")
            f.close()

    # This compares the actual solution to our predicted solution
    # and analyzes which lines were correctly and incorrectly predicted
    for i in range(len(predicted_solution)):
        if predicted_solution[i] == real_solution[i]:
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
