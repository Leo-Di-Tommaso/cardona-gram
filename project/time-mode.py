import random
import time
# from word_search import offline_lookup, online_lookup
from wordlist import gen_words, check_words, get_letters, check_words1

# compare input of the user to a dictonary
# I have no idea how to access the dictonary yet, there was no API
    
    
def main():
    points = 0
    # introduction to game
    print('Welcome to Anagrams!\nThis is a CS 32 Final Project\nMade by Leo, Tim and Ana')
    mama=input('Do you need instructions?(yes/no)')
    if mama=='yes':
        print('You will receive a letter set consisting out of 5 letters.\nGuess as many words as you can.\nYou may only use every letter ONCE.')
        print('You have 60 seconds per round to guess as many words as you can.')
    #use gen_words to get user input of how many letters he wants, and to create the letter_set
    
    while True:
        print('Creating a letter set now. This can take up to 2 minutes...')
        w, letters = check_words1()
    
        print(f'Your letter set is: {letters}')
        print(f'You have to guess {len(w)} word(s)')
        print('Timer starts now!')

        start=time.time()
        limit=60
        points_round=0

        while time.time()<= limit:

            word = input('Word: ')
            if word in w:
                points_round += len(word)
                print(f'That is a valid word! You earned {len(word)} points.')
                w.remove(word)
                print(f'You have {len(w)} words left to guess')

                if len(w)==0:
                    print('You guessed all the word. Congrats!')
                    break
            else:
                print('That is not a valid word! Try again!')
            
            
        print('Time is up!!!')
        print(f'You scored {points_round} points this round')
        points+=points_round

        check=input('Do you want to play another round? (yes/no)')
        if check != 'yes':
            print(f'Game Over! Your total score is {points} points.')
            break
            
                    
                        

if __name__ == '__main__':
    main()