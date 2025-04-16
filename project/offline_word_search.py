# pip install PyDictionary
from PyDictionary import PyDictionary as dictionary
def offline_lookup(word):
    if dictionary.meaning(word):
        # print(f"Definition: {dictionary[word]}")
        return True
    else:
        # print("Word not found.")
        return False
    
print(offline_lookup("word"))