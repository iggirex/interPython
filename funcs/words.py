import scrabble

alphabet = "abcdefghijklmnopqrstuvwxyz"

def isLetterDouble(letter):
    count = 0
    for word in scrabble.wordlist:
        if letter + letter in word:
            return count+1
    return count

# def checkLetter(letter):
#     count = 0
#     for letter in alphabet:
#         isLetterDouble(letter)
#         if true:
#             count+1
#     return count

for letter in alphabet:
    count = isLetterDouble(letter)
    if count == 0:
        print letter