# Rather than compute all possible permutations of the string, we instead opt to do a frequency analysis
# Simply check the frequency of a given string, and see if its frequency matches with any other string in the dictionary

import sys

def setup():
    if len(sys.argv) > 1:
        f = sys.argv[1]
    else:
        print("No file passed. Using path-to-dict.txt...")
        f = "path-to-dict.txt"
    return f

def divideIntoWords(dictionary):
    # Splits up my input, a big string of words,
    # into separate, smaller strings containing words
    s = dictionary.read()
    return s.split()

def getInput():
    # Get the user input dictionary
    userInput = input("Enter a string: ")
    if userInput == "":
        print("Error: No input found")
        print("Exiting... ")
        sys.exit(0)
    return userInput

def dictMe(string):
    # Conduct a frequency analysis on the string
    # Complexity of O(N), where N is the size of string
    # Mapping of character to number of times it appears in the string
    dictionary = {}
    for letter in string:
        if letter.lower() in dictionary:
            dictionary[letter.lower()] += 1
        else:
            dictionary[letter.lower()] = 1
    return dictionary

# Calling the functions

def main():
    f = setup()
    dictionary = open(f, "r")
    words = divideIntoWords(dictionary)
    s = set(words)

    # For each word in the dictionary, generate the frequency of the word
    # Then, store this in a mapping for ease of access

    # This is done so we don't need to create the frequency analysis for every iteration.
    # We can just do this in one-step, in the offline process

    wordFrequencies = {}
    for word in s:
        wordFrequencies[word] = (dictMe(word))

    user = getInput()

    while user:
        userFrequency = dictMe(user)

        toSort = set() # Set chosen to remove duplicates

        for element in s:
            if wordFrequencies[element] == userFrequency:
                toSort.add(element)

        if toSort:
            toSort = list(toSort) # Change to list to sort
            toSort.sort() # Sort
            for element in toSort:
                print(element, end = " ")
            print()
        else:
            print("-")

        user = getInput()

    dictionary.close()

main()
