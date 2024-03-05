def contains_all_vowels(string):
    string = string.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return all(vowel in string for vowel in vowels)

string = input("Enter a string: ")

if contains_all_vowels(string):
    print("The string contains all vowels.")
else:
    print("The string does not contain all vowels.")