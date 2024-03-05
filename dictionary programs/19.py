from collections import Counter

def largest_anagram_subset(words):
    sorted_letters_counter = Counter([''.join(sorted(word)) for word in words])
    largest_subset_size = max(sorted_letters_counter.values(), default=0)

    return largest_subset_size
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Size of the largest subset of anagram words:", largest_anagram_subset(words))