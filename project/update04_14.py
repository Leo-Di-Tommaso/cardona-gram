import random

def get_letters(length):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_set = random.sample(alphabet, int(length))
    return letter_set



# compare input of the user to a dictonary
# I have no idea how to access the dictonary yet, there was no API
import requests
def real_word():
    print('Searching Oxford Dictonary for your input')

    # Craft a request wikipedia 
    # url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={s}&srlimit=1&format=json"
    app_id =
    app_key =
    url= 'https://www.oed.com/discover/word-lists'

    headers = {'app_id':app_id, 'app_key':app_key}

    # Send that request from our computer to the one running wikipedia
    # Read the response from the wikipedia computer
    response = requests.get(url, headers=headers)

    # Print the answer to our question ... sorta
    if response.status_code == 200:
        print(f"The word exists!")
        return True
    else:
        print(f"The word does not exist")
        return False
    
    
def main():
    points = 0
    words_created = []
    # introduction to game
    print('Welcome to Anagrams!\nThis is a CS 32 Final Project\nMade by Leo, Tim and Ana')
    print('You can work with a set of letters of length 5 to 10.')
    while True:
        num = input('Enter how many letters you want to work with: ')
        if 5 <= num <= 10:        
            letters = get_letters(num)
            break
        else:
            print('Number must be between 5 and 10. Try again.')
    # start game
    print(f'Your letter set is: {letters}')
    print('You may now begin finding words with this letter set!')
    while True:
        word = input('Word: ')
        if word in # database of valid words?:
            points += len(word)
            print(f'That is a valid word! You earned {len(word)} points and are now at {points} total points')
            words_created.append(word)
        else:
            print('That is not a valid word!')
        checkpoint = input('Would you like to continue?\nType Y for yes and N for no: ')
        if checkpoint == 'N':
            break

if __name__ == '__main__':
    main()