import csv
def csv_search(word):
    word = word.capitalize()
    with open('c:/Users/Leonardo/Documents/GitHub/cardona-gram/project/files/dictionary.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if word in row[0]:
                print(word)
                return True
            
            
csv_search("alphabet")