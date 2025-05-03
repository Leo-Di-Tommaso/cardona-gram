import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter_set = random.sample(alphabet, 5)

print(letter_set)




# compare input of the user to a dictonary
import requests
def real_word():
    print('Searching Oxford Dictonary for your input')

    # Craft a request wikipedia will understand about The Cat in the Hat
    s = 'The Cat in the Hat'.replace(' ', '+')
    # url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={s}&srlimit=1&format=json"
    url= 'https://www.oed.com/discover/word-lists'

    # Send that request from our computer to the one running wikipedia
    # Read the response from the wikipedia computer
    response = requests.get(url)

    # Print the answer to our question ... sorta
    if response.status_code == 200:
        print(f"The word exists!")
    else:
        print(f"The word does not exist")

if __name__ == '__real_word__':
    real_word()