import json
from typing import List

with open('words_dictionary.json', 'r') as f:
    word_dict = json.load(f)

dictionary_list = list(word_dict)

# Source for dictionary json - mixture of en-US and en-UK words
# https://github.com/dwyl/english-words

# the array of prohibited letters that I have interpreted from the email
prohib_letters = ['j', 'k', 'z', 'c', 'q', 'v']


# Checks for prohibited letters in the string passed - compares each character in string with each letter from
# prohibited letter array
def checkletters(word):
    """
    :param word: a word to check for prohibited letters as in probib_letters array
    :return: True if no prohibited characers in word
    """
    for i in range(0, len(word)):
        for x in prohib_letters:
            if word[i] == x:
                return False
    return True


# Goes through list of all added words and removes any that have fewer characters than the known maximum
def reducelist(list, length):
    """
    :param list: a list of strings to be reduced to only ones meeting length
    :param length: a length stating the length that the output strings must be
    :return: a list of strings from input list where the element length = length
    """
    output: List[any] = []
    for v in list:
        if len(v) == length:
            output.append(v)
    return output


# Produces a string the is more human readable than printing a list - adds commas and 'and' when necessary
def visualstringlist(list):
    """
    :param list: a list to modified to human natural reading presentation
    :return: a string of all elements from list with commas and 'and' as relevant for natural reading
    """
    string = ""
    if len(list) == 1:
        return list[0]
    for c in list:
        if c == list[len(list) - 1]:
            string = string + " and " + c
        else:
            string = string + " " + c + ","
    return string


# Prints the output to the colsole in a readable manner
def displayoutput(list):
    """
    :param list: a list of words as the result from checking to be presented to the user
    :return: N/A
    """
    letters = visualstringlist(prohib_letters)
    words = visualstringlist(list)

    print("From the provided dictionary " + str(len(list)) + " word(s) have been found not including the ")
    print("prohibited letters: " + letters)
    print("\nThe word(s) had a length of " + str(maxLength) + " characters and were: " + words)


maxLength = 0
longWords = []

# Iterates through list starting at max length of 0, if word k has a greater length then it is checked for prohibited
# letters and then the max length is increased if it is valid
for k in dictionary_list:
    if len(k) >= maxLength:
        if checkletters(k):
            maxLength = len(k)
            longWords.append(k)

# Reduces the list length and outputs the results
longWords = reducelist(longWords, maxLength)
displayoutput(longWords)
