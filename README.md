# cardona-gram
Repository for the CS 32 final project of Ana Isabel Cardona, Leonardo Di Tommaso and Tim Langenbahn

Anagram game & solver, which gives a user a set of letters to create words with and provides all possible solutions after the game is over 
- the program picks a random x letters from the alphabet
- then checks all the possible combinations in a dictionary (web search) or library to see if they are actual words
- the player is given the letters and they try to guess the anagrams
- the computer checks the client's guesses against it's list of words to see if they are real words
- if the player passes the first round and guesses all the anagrams, the difficulty is increased by changing the weight of the possible lengths of the words to make them longer on average 
(so that the first round there is a higher chance of getting words with 3 or 4 letters and if the player guesses all the anagrams within a certain number of tries then the second round there is a higher chance of getting words that are long between 5 and 6 letters)
