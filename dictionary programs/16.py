def group_anagrams(words):
    anagrams_dict = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]

    for anagrams in anagrams_dict.values():
        print(anagrams)

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(words)