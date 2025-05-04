# cardona-gram
Repository for the CS 32 final project of Ana Isabel Cardona, Leonardo Di Tommaso and Tim Langenbahn

Anagram game & solver, which gives a user a set of letters to create words with and provides all possible solutions after the game is over 
- the program picks a random x letters from the alphabet
- then checks all the possible combinations in a dictionary (web search) or library to see if they are actual words
- the player is given the letters and they try to guess the anagrams
- the computer checks the client's guesses against it's list of words to see if they are real words
- return the list of words the computer found
- if the player passes the first round and guesses all the anagrams, the difficulty is increased by changing the weight of the possible lengths of the words to make them longer on average 
(so that the first round there is a higher chance of getting words with 3 or 4 letters and if the player guesses all the anagrams within a certain number of tries then the second round there is a higher chance of getting words that are long between 5 and 6 letters)



In the word_search.py you can find all of the functionas that we considered using to check if a combination of letters was an actual word. We created 3 versions: an online search that uses an API and checks for words there, a first offline search which uses the enchant library to check if a combination of letters is a word and, finally, a second offline search, which uses a CSV file from the following github: https://github.com/pkLazer/password_rank/blob/master/4000-most-common-english-words-csv.csv. We decided to go for the third option, as it was giving us more common words and it was using a way shorter runtime. Additionally, this choice allowed us not to have to worry about the client knowing many uncommon acronyms. 