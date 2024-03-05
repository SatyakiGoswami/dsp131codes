
words = ["apple", "banana", "cat", "dog", "elephant", "zebra"]

def is_ordered(word):
    return list(word) == sorted(word)

ordered_words = [word for word in words if is_ordered(word)]

print("Ordered words:", ordered_words)