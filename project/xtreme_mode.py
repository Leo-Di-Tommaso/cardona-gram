import time
from wordlist import check_words3

def time_mode():
    '''This function allows the player to play the time gamemode, where the the user has to write as many anagrams as possible in 1 minute from one or more letter sets. 
    It creates a list of letters, then a list of words that the player has to gueess. Then, a timer starts and the player has to input words which are then checked against the
    previously generated list of words. Each word gives the player as many points as there are letters in it. Once every word is guessed for a letter set, another one is generated
    until the player runs out of time.'''
    points = 0

    # introduction to game 
    if input('Do you need instructions? (yes/no) ') == 'yes':
        print('You will receive a letter set consisting out of 5 letters.\nGuess as many words as you can.' \
        '\nYou may only use every letter ONCE. \nYou have 60 seconds and 3 lives to guess as many words as you can.' \
        '\nIf you find all the words to one letter set, a new one will be generated.\nThe game ends if you run out of lives or hearts.\nTake care of your hearts! Each heart equals additional two points in the end.')

    input('If you are ready to start press any key')
        
    while True:            # game loop
        #generate words and letters
        lives =3
        w, letters = check_words3()
        print(f'Your letter set is: {letters}')
        print(f'You have to guess {len(w)} word(s)')
        hearts = lives * "\u2764\ufe0f " 
        print(f'You have {hearts} lives.')
    
        print('Timer starts now!')
        
        points_round=0
        guessed_words=[]
        

        start_time = time.time() # look at initial UTC time of the game
        while time.time() - start_time <= 60 and lives >0: #check if more than 60s passed from the initial UTC time
            word = input('Word: ')
            if word in w: 
                points_round += len(word)
                print(f'That is a valid word! You earned {len(word)} points.')
                w.remove(word)
                guessed_words.append(word)
                print(f'You have {len(w)} words left to guess in {letters}. You already guessed {guessed_words}')

                if len(w) == 0:
                    print('You guessed all the words in this letter set!')
                    w, letters = check_words3()
                    print(f'Your letter set is: {letters}')
                    print(f'You have to guess {len(w)} word(s)')
                    
            else:
                lives=lives-1
                hearts = lives * "\u2764\ufe0f " 
                print('That is not a valid word! Try again!')
                if lives !=0:
                    print(f'You have {hearts} lives.')

        print('Game Over!!!')
        if lives ==0:
            print('You ran out of lives!')
            print(f'You scored {points_round} points.')

        else:
            print('You ran out of time!')
            print(f'Lives left: {hearts} (+{2*lives} points)')
            points_round = points_round + 2*lives
            print(f'You scored {points_round} points.')
        
        points+=points_round
        print(f'You did not guess {w}')
        
    


        check = input('Do you want to play another round? (yes/no) ')
        if check != 'yes':
            print(f'Game Over! Your score is {points} points.')
            break

def main():      
    time_mode()
                        

if __name__ == '__main__':
    main()