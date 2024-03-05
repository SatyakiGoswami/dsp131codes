def remove_duplicates(sentence):
    words = sentence.split()
    unique_words = set(words)

    unique_sentence = ' '.join(unique_words)

    return unique_sentence
sentence = "the quick brown fox jumps over the lazy dog the quick brown fox"
unique_sentence = remove_duplicates(sentence)
print("Original sentence:", sentence)
print("Sentence with duplicates removed:", unique_sentence)