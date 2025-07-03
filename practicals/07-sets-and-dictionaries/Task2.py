#Letters that appear in at least one of the two words.
def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))
print(letters_in_either("Green", "Land"))

#Letters that appear in both words.
def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))
print(letters_in_both("Green", "Land"))

#Letters that appear in either word, but not in both.

def letters_in_one_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))
print(letters_in_one_not_both("gREEN", "Land"))

