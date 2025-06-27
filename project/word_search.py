# this file has our functions which make sure words are exist in English

# CSV LOOKUP:
import csv
import os
def csv_search(word):
    '''This function, given a word, checks if it's an actual word by checking it against a csv file with approximately 4000 of the most common English words'''
    file_path = os.path.join("project","files","4000-most-common-english-words-csv.csv")
    # file_path = os.path.join("project","files","it_full.csv")
    # file_path = os.path.join("project","files","wordlist.10000.csv")
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if word in row[0] and len(row[0]) == len(word):
                return True
            # else:
                # return False
    return False


# ONLINE LOOKUP:
import requests as r
def online_lookup(word):
    '''This function, given a word, checks if it's an actual word by checking it against an online API English dictionary'''
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = r.get(url)
    if response.status_code == 200:
        # print(f"DEBUG: {word} is a word!")
        return True
    else:
        return False



# OFFLINE LOOKUP:
# pip install PyDictionary
import enchant
def offline_lookup(word):
    '''This function, given a word, checks if it's an actual word by checking it against a dictionary from the enchant library'''
    d = enchant.Dict("en_US")
    if d.check(word) == True:
        return True
    else:
        return False