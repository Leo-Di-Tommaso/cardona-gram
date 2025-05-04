# cardona-gram
Repository for the CS 32 final project of Ana Isabel Cardona, Leonardo Di Tommaso and Tim Langenbahn

word_search.py 
In this file, you can find all of the functions we build that could be used to check if a specific combination of letters is a valid English word. We created three versions: 
1) An online search which uses an API which we used in the same way that we learnt to look up things on HOLLIS and Wikipedia in class. 
2) An offline search which uses the enchant library which would need to be imported and which was giving us a lot of issues with compatibility and storage. We found out how to use it from this website
3) A second offline search which uses a CSV file from the following Github: https://github.com/pkLazer/password_rank/blob/master/4000-most-common-english-words-csv.csv It is flawed in the sense that the English language has over 170,000 words, so it does not recognize some words that are not as common during the game. We considered using the MIT word list csv file, but it contained far too many acronyms and other words which do not actually exist. 
We decided to use the third option, as it was giving us more common words (as opposed to acronyms or surnames) and had a much shorter runtime. Additionally, it allows for the game to be played without having to install a Python library or any files. 

wordlist.py 
The functions in this file first create a list of letters. Then, using the permutation methods (which we learnt how to use by looking at this guide), they create all possible combinations of the given letters that are 3 or more letters in length, and check their validity by calling the appropriate function from word_search.py. One issue we ran into was that some randomized letter sets did not have any possible valid combinations; to tackle this, we created the function check_list, which creates new letter sets and word lists until it finds one that has at least one valid word. 

newest5.py  
This is the main body of our project, the code which runs the game. It reads the user game instructions, creates a letter set, which it prints to the user, and a wordlist, which is used to check if user submissions are correct. The user is also told the length of the wordlist, and continually reminded of how many possible words are left to guess. The user wins points based on the length of the words they are created: for each letter they use in a valid word, they get one point. This is the most basic version of the game, where the user can play an infinite number of letter sets and the game ends solely upon user request.

survival-mode3.py 
This is another game mode which we added for complexity once we had figured out the basic game. It is similar to newest5.py, but it implements a “three-lives” system, where the user has to write as many anagrams as possible without making mistakes, and can only input three incorrect words before the game ends. Once every possible word is guessed for one letter set, another one is generated until all three lives are lost. 

time-mode.py  
This is a third game mode, which is the basic game but with a timer function. The user has 60 seconds to earn as many points as they can before the game ends by guessing words. If the player guesses every possible word before the time is up, a new letter set is generated and the timer continues. The goal here is to get as many points as possible as time runs out. 
