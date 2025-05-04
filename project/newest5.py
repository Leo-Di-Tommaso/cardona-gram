from wordlist import check_words_5_t_10
  
def main():
    points = 0
    # introduction to game
    print('Welcome to Anagrams!\nThis is a CS 32 Final Project\nMade by Leo, Tim and Ana')
    instructions = input('Do you need instructions? (yes/no): ')
    if instructions == 'yes':
        print('You will receive a letter set consisting of 6 letters.\nGuess as many words as you can.\nYou may only use every letter ONCE in each word.')
        
    # start game
    while True:

        print('Creating a letter set now...')

        w, letters = check_words_5_t_10()
        print(f'Your letter set is: {letters}')
        print(f'Possible words: {len(w)}')
        print('You may now begin finding words with this letter set!')



        while True:
            word = input('Word: ')
            if word in w:
                points += len(word)
                print(f'That is a valid word! You earned {len(word)} points and are now at {points} total points')
                w.remove(word)
                print(f'You have {len(w)} word(s) left to guess in {letters}')
                if len(w)==0:
                    break       
            else:
                print('That is not a valid word! Try again!')

        checkpoint = input('You guessed all the words. Do you want to play another round?\nType "x" to end the game, or any other key to continue: ')
        if checkpoint == 'x':
            print(f'Game Over! Your total score is {points} points.')
            break
        else:
            print('Good job so far! You will receive a new set of letters now.')  

if __name__ == '__main__':
    main()