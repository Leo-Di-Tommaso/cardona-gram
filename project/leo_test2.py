import requests

def lookup_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

data = lookup_word("hello")
print(data[0]["meanings"][0]["definitions"][0]["definition"])
