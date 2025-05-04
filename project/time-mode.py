import time
from wordlist import check_words3


    
def main():
    points = 0
    # introduction to game
    print('Welcome to Anagrams!\nThis is a CS 32 Final Project\nMade by Leo, Tim and Ana')
    mama=input('Do you need instructions?(yes/no) ')
    if mama=='yes':
        print('You will receive a letter set consisting out of 5 letters.\nGuess as many words as you can.\nYou may only use every letter ONCE.')
        print('You have 60 seconds per round to guess as many words as you can.')
    #use gen_words to get user input of how many letters he wants, and to create the letter_set
    checkpoint=input('If you are ready to start press any key')
    while True:
        print('Creating a letter set now. This can take up to 2 minutes...')
        w, letters = check_words3()
    
        print(f'Your letter set is: {letters}')
        print(f'You have to guess {len(w)} word(s)')
        print('Timer starts now!')

        
        points_round=0
       
        start_time = time.time()
        
        while time.time() - start_time <= 30:
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