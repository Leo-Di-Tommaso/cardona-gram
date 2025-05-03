import random
from word_search import gen_words
def get_letters(length):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_set = random.sample(alphabet, int(length))
    return letter_set



# compare input of the user to a dictonary
# I have no idea how to access the dictonary yet, there was no API
    
    
def main():
    points = 0
    # introduction to game
    print('Welcome to Anagrams!\nThis is a CS 32 Final Project\nMade by Leo, Tim and Ana')
    #use gen_words to get user input of how many letters he wants, and to create the letter_set
    while True:
        w, letters = gen_words()
        if len(w)!=0:
            print(f'Your letter set is: {letters}')
            print(f'You have to guess {len(w)} words')
            break
        else:
            print('Created a list with 0 existing words. I will create a new one')
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
                    while True:
                        w, letters = gen_words()
                        if len(w) !=0: 
                            print(f'Your letter set is: {letters}')
                            print(f'You have to guess {len(w)} words')
                            break
                        else:
                            print('Created a list with 0 existing words. I will create a new one')
                    continue
        else:
            print('That is not a valid word! Try again!')

if __name__ == '__main__':
    main()