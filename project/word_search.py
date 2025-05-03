# this file has our functions which make sure words are exist in english

# CSV LOOKUP: c:/Users/timla/OneDrive
import csv
import os
def csv_search(word):
    # word = word.capitalize()
    file_path = os.path.join("project","files","4000-most-common-english-words-csv.csv")
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if word in row[0] and len(row[0]) == len(word):
                print(word)
                return True
        

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




# pip install PyDictionary
# OFFLINE LOOKUP:

import enchant
def offline_lookup(word):
    d = enchant.Dict("en_US")
    if d.check(word) == True:
        return True
    else:
        return False