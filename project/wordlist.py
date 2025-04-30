# this document generates a list of words to use for the game
# in this copy i removed the ability for user to choose length of letter set
import random
from word_search import online_lookup, offline_lookup
from itertools import permutations
import enchant

def get_letters():
    '''creates a list of random letters to be used in the game'''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_set = random.sample(alphabet, 6)
    return letter_set

def gen_words(letters):
    '''This function recalls the function get_letters(). it then uses the list of letters to 
    create permutations of the letters with different lenghts. the permutations are then joined together into words 
    and checked in an online dictionary. if they exist, they are added to a list of words that exist that the client 
    will then try to guess'''
    words = []
    # letters = get_letters()
    print(f'DEBUG {letters}')

    ## create permutations 
    for k in range(3,7,1):
        combinations = [''.join(x) for x in permutations(letters, r=k)]
        for word in combinations:
            if online_lookup(word): 
            # if offline_lookup(word):
                words.append(word)                                  
    print(f'DEBUG: the possible words with the generated letters are: {words}')
    return words 

def check_words():
    '''this function makes sure that the generated word list has at least 5 possible words, otherwise the game
    can't really work'''
    while True:
        letters = get_letters()
        wordlist = gen_words(letters)
        if len(wordlist) >= 5:
            return wordlist and letters # because we need letters for main()
            break

check_words()
