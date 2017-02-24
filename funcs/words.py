import scrabble

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# def isLetterDouble(letter):
#     count = 0
#     for word in scrabble.wordlist:
#         if letter + letter in word:
#             return count+1
#     return count
#
# for letter in alphabet:
#     count = isLetterDouble(letter)
#     if count == 0:
#         print letter

vowels = "aeiou"

def areAllVowelsInWord(word):
    count = 0
    for vowel in vowels:
        if vowel in word:
            count = count + 1
    if count == 5:
        return True

for word in scrabble.wordlist:
    if areAllVowelsInWord(word):
        print (str(word) + " has all the vowels in it")