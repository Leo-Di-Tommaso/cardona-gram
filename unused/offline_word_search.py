# pip install PyDictionary
import enchant

def offline_lookup(word):
    d = enchant.Dict("en_US")
    if d.check(word) == True:
        return True
    else:
        return False
    