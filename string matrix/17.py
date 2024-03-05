def find_words_greater_than_k(string, k):
    words = string.split() 
    result = [word for word in words if len(word) > k]
    return result


sentence = "This is a sample sentence with words of different lengths"
k = 4
long_words = find_words_greater_than_k(sentence, k)
print(f"Words longer than {k} characters: {long_words}")