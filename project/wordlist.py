import random
from word_search import lookup_word
from itertools import permutations

def get_letters(length):
    '''given a number, it creates a list of random letters of the length requested'''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_set = random.sample(alphabet, int(length))
    return letter_set

def gen_words():
    '''Given a number, the function recalls the function get_letters(length). it then uses the list of letters to 
    create permutations of the letters with different lenghts. the permutations are then joined together into words 
    and checked in an online dictionary. if they exist, they are added to a list of words that exist that the client 
    will then try to guess'''
    words = []
    word = ""
    w = []
    # print('You can work with a set of letters of length 5 to 10.')
   # while True:
    num = int(input('Enter how many letters you want to work with: '))
        # if 5 <= num <= 10:        
    letters = get_letters(num)
            # break
        # else:
        #     print('Number must be between 5 and 10. Try again.')
    print(f'DEBUG {letters}')
    for k in range(num):
        words += list(permutations(letters, r = k))
#    print(words)
    for i in range(len(words)):
        word = word.join(words[i]) # "this line is the enemy"     -Tim
        # print(f'DEBUG: {word}')
        if lookup_word(word):
            w.append(word)

    print(w)

gen_words()
