import json
import random
from typing import List
from tkinter import *


with open('dictionary.json', 'r') as f:
    word_dict = json.load(f)

dictionary_list = list(word_dict)
print(len(dictionary_list))

# Source for dictionary json - mixture of en-US and en-UK words
# https://github.com/dwyl/english-words

# the array of given letters
given_letters = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
prohib_letters = list(set(alphabet)-set(given_letters))


# Checks for given letters in the string passed - compares each character in string with each letter from
# given letter array
def checkletters(word):
    """
    :param word: a word to check for prohibited letters as in probib_letters array
    :return: True if no prohibited characers in word
    """
    temp_letters = given_letters.copy()

    for i in range(0, len(word)):
        if letterpresent(word[i], temp_letters):
            temp_letters.remove(word[i])
        else:
            return False
    return True


# dependancy for checking letters, takes a letter and list of letters and returns true if there is a match
def letterpresent(letter, list):
    """
    :param letter: a letter to check against
    :param list: a list of given letters
    :return: True if there is a match between the check letter and given letters
    """
    for l in list:
        if l == letter:
            return True
    return False


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


def top10():
    unsorted_list = []
    for w in dictionary_list:
        if checkletters(w):
            unsorted_list.append(w)
    sortedlist = sorted(unsorted_list, key=len)
    return sortedlist[-9:]


# Produces a string the is more human readable than printing a list - adds commas and 'and' when necessary
def visualstringlist(list):
    """
    :param list: a list to modified to human natural reading presentation
    :return: a string of all elements from list with commas and 'and' as relevant for natural reading
    """
    string = ""
    if len(list) == 1:
        return list[0]
    for c in range(0, len(list)):
        if c == len(list) - 1:
            string = string + " and " + list[c]
        else:
            string = string + " " + list[c] + ","
    return string


# Prints the output to the console in a readable manner
def displayoutput(list, top10, maxLength):
    """
    :param list: a list of words as the result from checking to be presented to the user
    :return: N/A
    """
    letters = visualstringlist(given_letters)
    words = visualstringlist(list)

    res = "From the provided dictionary " + str(len(list)) + " word(s) have been found from the "
    res += "given letters: " + letters
    res += "\nThe word(s) had a length of " + str(maxLength) + " characters and were: " + words
    res += "\n\nthe top 10 answers were:"

    info.configure(text=res)

    colours = ['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7', '#C7CEEA']
    colourcounter = 5

    counter = 3
    for w in top10:
        # print(f'\n{w}: {word_dict[w]}')
        colour = colours[colourcounter]
        a = Label(window, text=w, bg=colour, wraplength=500)
        a.grid(column=0, row=counter)

        b = Label(window, text=word_dict[w], bg=colour, wraplength=1500)
        b.grid(column=1, row=counter)
        counter += 1
        colourcounter -= 1
        if colourcounter == -1:
            colourcounter = 5


def getdefinition(word):
    for x in range(0, len(word_dict)):
        if word == word_dict[x]:
            return


def runcalculation():
    # delete items from grid
    for label in window.grid_slaves():
        if int(label.grid_info()["row"]) > 2:
            label.grid_forget()

    maxLength = 0
    longWords = []

    given_letters.clear()
    string = letters.get().lower()
    for a in string:
        given_letters.append(a)

    # Iterates through list starting at max length of 0, if word k has a greater length then it is checked for prohib
    # letters and then the max length is increased if it is valid
    for k in dictionary_list:
        if len(k) >= maxLength:
            if checkletters(k):
                maxLength = len(k)
                longWords.append(k)

    # Reduces the list length and outputs the results
    longWords = reducelist(longWords, maxLength)
    bestanswers = top10()
    displayoutput(longWords, bestanswers, maxLength)


def testfunc():
    print("test function sucessful")


# Tkinter UI

window = Tk()
window.title("Countdown Solver")
window.geometry('1920x1080')


# create widgets
button = Button(window, text="Run", command=runcalculation)
button.grid(column=0, row=0, columnspan=2)

letters = Entry(window)
letters.grid(column=0, row=1, columnspan=2)

info = Label(window, text="Info will appear here")
info.grid(column=0, row=2, columnspan=2)

window.mainloop()
