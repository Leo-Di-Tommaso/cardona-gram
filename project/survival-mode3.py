import random
# from word_search import offline_lookup, online_lookup
from wordlist import gen_words, get_letters, check_words1

# compare input of the user to a dictonary
# I have no idea how to access the dictonary yet, there was no API
    
    
def survival():
    '''This function allowes the player to play the survival gamemode, where the the user has to write as many anagrams as possible more letter sets without making mistakes. 
    It creates a list of letters, then a list of words that the player has to gueess. Then, a timer starts and the player has to input words which are then checked against the
    previously generated list of words. Each word gives the player as many points as there are letters in it. Once every word is guessed for a letter set, another one is generated.
    The player starts with 3 hearts. Rvery time the player guesses a word that is not an english word, they lose a heart.'''
    points = 0
    lives = 3
    # introduction to game
    print('Welcome to Anagrams!\nThis is a CS 32 Final Project\nMade by Leo, Tim and Ana')
    instructions = input('Do you need instructions?(yes/no): ')
    if instructions == 'yes':
        print('You will receive a letter set consisting of 5 letters.\nGuess as many words as you can.\nYou may only use every letter ONCE for each word.\nYou have 3 lives. If you guess a nonexistent word, you lose a life.\nGet as many points as you can!')

    # start game
    print('You may now begin finding words with this letter set!')
    while lives > 0:
        #use gen_words to get user input of how many letters he wants, and to create the letter_set
        w, letters = check_words1()
        print(f'Your letter set is: {letters}')
        print(f'Possible words: {len(w)}')
        hearts = lives * "\u2764\ufe0f " 
        print(f'You have {hearts} lives.')
        # user guesses
        while len(w) > 0 and lives > 0:
            word = input('Word: ')
            if word in w:
                points += len(word)
                print(f'That is a valid word! You earned {len(word)} points and are now at {points} total points')
                w.remove(word)
                print(f'You have {len(w)} word(s) left to guess')
            else:
                print('That is not a valid word!')
                lives -= 1
                hearts = lives * "\u2764\ufe0f " 
                print(f'you have {hearts} lives left.')
                if lives == 0:
                    print(f'Game Over. Your final score is {points} points.')
                    break
        if lives > 0:
            print('Good job so far! You will receive a new set of letters now.')

def main():
    survival()

if __name__ == '__main__':
    main()