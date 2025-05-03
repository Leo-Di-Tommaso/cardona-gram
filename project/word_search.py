# this file has our functions which make sure words are exist in english

# ONLINE LOOKUP:
import requests as r

def online_lookup(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = r.get(url)
    # if response.status_code != 200:
    #     return None
    # return response.json()
    if response.status_code == 200:
        print(f"DEBUG: {word} is a word!")
        return True
    else:
        # print(f"DEBUG: The word does not exist")
        return False

# data = lookup_word("lion")
# print(data[0]["meanings"][0]["definitions"][0]["definition"])

# ONLINE LOOKUP:
# pip install PyDictionary
import enchant

def offline_lookup(word):
    d = enchant.Dict("en_US")
    if d.check(word) == True:
        return True
    else:
        return False