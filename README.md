Description:
Rather than generating all permutations of the dictionary words and checking that an element is one of the N! permutations, we simply conduct a frequency analysis on each string and check that their frequencies match
The idea is as follows:
Split our input into a series of strings, our words, and generate the frequencies for each word. Generating frequencies for a given string is a linear-time operation, since we simply parse the string and count the occurrences of the characters.
Then, get the user input, get its frequency, and check each dictionary frequency and see if there's a match.
Sort the resulting list at the very end and print

Note: Another idea is to sort each string in our dictionary and check that the user sorted input and a dictionary sorted input are identical. I found this solution to be more natural and efficient.

1)
Offline:

setup: Simply parsing the file name provided or using a default. O(B), where B is the file name, but this is unlikely to be the deciding factor in the overall Complexity

divideIntoWords: Take the big string of words in the file and divide it into each word. Assuming there are N words in this file, this is O(N)

dictMe: For a provided string, do a frequency analysis where we break up the string into its character count (ex: hello becomes {'h': 1, 'e': 1, 'l': 2, 'o': 1})
The complexity of this for a string of length K is O(K), since we simply iterate over the string and keep count of characters seen.

Creating word frequencies: For each string in the file, generate its frequency analysis. Since there are N words in this file, and assuming worst-case string length of L, the worst-case runtime of this is O(NL)

After the above steps, we can take in user input and conduct the analysis. The overall worst-case bound for the offline process (processing the file) is O(NL), as this is the most exhaustive part of the offline process

Online:

Get user input: Built-in function, assuming U is the length of the user input, this is O(U)

Generate frequency of user input: O(U), because again we are iterating over the user string and counting the occurrences of the characters

Iterating over our dict and checking if the frequencies match: Assuming our dictionary is of size N (since there are N words in our file), we check if the frequencies match (if they do, we put the word from the dictionary in a set). Since our frequencies are dictionaries, we must manually iterate over each element of the dictionary and ensure they matches
In the worst case, this will take O(U), since the matching will not be equal if the considered element exceeds U length. Over all words, this is O(NU).

Sorting: At the end, we sort our results. This is using python's built-in quicksort, which has worst-case bound O(N^2), but in extremely improbable circumstances having to do with pivots. The expected runtime is Nlog(N), where N is again the number of words of our dictionary (since, in worst-case, every word of the dictionary will be an anagram of the considered word)

Printing: Simply iterate over our list and print out each element. This is worst-case the length of this list, which is O(N)

After the above steps, we are ready to take another user input. For one iteration of a given input, the complexity is O(max(NU, Nlog(N))), meaning the quicksort or frequency check can be exhaustive depending on if U > log(N)
For K iterations, this is O(K * max(NU, Nlog(N)))

2)
Since we are storing a frequency analysis of each string in our dictionary, and we have N words in our dictionary, and each frequency dictionary can have A characters (where A is the size of the alphabet), this can be O(NA).

3)
An idea to deal with limited memory is to take each frequency breakdown and hash the frequency, then store those hashes in some set.
Then, take our user input and create its frequency, and hash it. If the hash is within the set, it's likely an anagram (since the probability of a collision when the two elements are not identical is incredibly small via the cryptographic hash properties)
The problem here is that we cannot return the string corresponding to the anagram, because we cannot hold all the strings of the dictionary due to limited memory. Effectively, this is like a bloom filter of sorts, by detecting if an anagram exists but unable to claim what that anagram is

Another idea is to divide our dictionary into chunks our memory can handle. We consider the maximum number of words and their corresponding frequencies we can fit given the limited memory, and check those contents via the algorithm implemented here. Then, repeat with a new set, and do this over and over until we exhaust the dictionary.
We print out the elements, never store them, so we can repeat this process over multiple iterations until we completely cover the dictionary.
The runtime depends on how many chunks we can divide our dictionary into while still staying within memory constraints:
Assuming K chunks, and knowing that our runtime is O(max(NU, Nlog(N))), this will take O(K * max(NU, Nlog(N)))
(Note: we cannot guarantee the lexicographic ordering because we are printing these elements out in some order dependent on which chunk we are in. We guarantee that the anagrams will be correct, but we cannot guarantee they are in the same order because we cannot store all these anagrams due to memory constraints)
