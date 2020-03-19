'''Isogram Detector :: Check if word has no repeating letters'''

word = input()

print( "true" if len(word) == len(set(word)) else "false" )