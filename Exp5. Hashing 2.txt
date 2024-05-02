import random

def custom_hash(input_string):
    ascii_sum = sum(ord(char) for char in input_string)
    mod_value = ascii_sum % 11
    random_int = random.randint(10, 1000)
    hashed_value = mod_value + random_int
    return hashed_value

input_string = input("Enter a string to hash: ")
hashed_value = custom_hash(input_string)
print("Hashed value:", hashed_value)
