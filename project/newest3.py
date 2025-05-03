import random
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
    #use gen_words to get user input of how many letters he wants, and to create the letter_set
    print('Creating a letter set now. This can take up to 2 minutes...')
    w, letters = check_words1()
    
    print(f'Your letter set is: {letters}')
    print(f'You have to guess {len(w)} word(s)')

        
    # start game
    print('You may now begin finding words with this letter set!')
    while True:
        word = input('Word: ')
        if word in w:
            points += len(word)
            print(f'That is a valid word! You earned {len(word)} points and are now at {points} total points')
            w.remove(word)
            print(f'You have {len(w)} words left to guess')
            if len(w)==0:
                checkpoint = input('You guessed all the words. Do you want to continue (yes/no)?')
                if checkpoint == 'no':
                    print(f'Game Over! Your total score is {points} points.')
                    break
                else:
                    print('Good job so far! You will receive a new set of letters now.')
                    print('Creating a new letter set. This can take up to 2 minutes...')
                    
                    w, letters = check_words1()
                    print(f'Your letter set is: {letters}')
                    print(f'You have to guess {len(w)} words')
                   
                    
        else:
            print('That is not a valid word! Try again!')

if __name__ == '__main__':
    main()