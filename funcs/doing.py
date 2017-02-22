def starts_with_a_vowel(word):
    return word[0] in "AEIOU"

x = starts_with_a_vowel("Iggi")

print x


names = ["Alice", "Bob", "Cara", "Editch"]
def filter_to_vowel_words(word_list):
    vowel_words = []
    for word in word_list:
        if starts_with_a_vowel(word):
            vowel_words.append(word)
    return vowel_words
print filter_to_vowel_words(names)
