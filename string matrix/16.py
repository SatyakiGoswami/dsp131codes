import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_until_match(target_string):
    length = len(target_string)
    generated_string = generate_random_string(length)
    attempts = 1

    while generated_string != target_string:
        generated_string = generate_random_string(length)
        attempts += 1

    print(f"Target string '{target_string}' generated after {attempts} attempts.")

# Example usage:
target_string = "HelloWorld123"
generate_until_match(target_string)