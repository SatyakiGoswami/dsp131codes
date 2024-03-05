
words = ["apple", "banana", "cat", "dog", "elephant", "zebra"]

def find_possible_words(characters):
    possible_words = []
    for word in words:
        if all(char in word for char in characters):
            possible_words.append(word)
    return possible_words

given_characters = "aeppl"
possible_words = find_possible_words(given_characters)
print("Possible words using given characters:", possible_words)