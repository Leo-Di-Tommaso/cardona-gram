from wordlist import check_words_5_t_10
  
def cardonagrams():
    '''This function allows the player to play the basic gamemode, where the the user has to write as many anagrams as possible given a list of letters. 
    It creates a list of letters, then a list of words that the player has to guess. Then, the player has to input words which are then checked against the
    previously generated list of words. Each word gives the player as many points as there are letters in it. Once every word is guessed for a letter set, another one is generated.'''
    points = 0

    # introduction to game
    print('Welcome to Anagrams!\nThis is a CS 32 Final Project\nMade by Leo, Tim and Ana')
    instructions = input('Do you need instructions? (yes/no): ')
    if instructions == 'yes':
        print('You will receive a letter set consisting of 6 letters.\nGuess as many words as you can.\nYou may only use every letter ONCE in each word.')
        
    
    while True: # game loop
        guessed_words = []
        print('Creating a letter set now...')

        # create a letter set of 6 letters with 5 to 10 possible words to find.
        w, letters = check_words_5_t_10()
        
        print(f'Your letter set is: {letters}')
        print(f'Possible words: {len(w)}')
        print('You may now begin finding words with this letter set!')

        # while True loop for every letter set
        while True:
            word = input('Word: ')
            if word in w:
                points += len(word)
                print(f'That is a valid word! You earned {len(word)} points and are now at {points} total points')
                w.remove(word)
                guessed_words.append(word)
                print(f'You have {len(w)} word(s) left to guess in {letters}. You already guessed {guessed_words}')
                if len(w)==0:
                    break       
            else:
                print('That is not a valid word! Try again!')

        checkpoint = input('You guessed all the words. Do you want to play another round?\nType "x" to end the game, or any other key to continue: ')
        # The only way for the game to end
        if checkpoint == 'x':
            print(f'Game Over! Your total score is {points} points.')
            break
        else:
            print('Good job so far! You will receive a new set of letters now.')  


def main():
    cardonagrams()


if __name__ == '__main__':
    main()