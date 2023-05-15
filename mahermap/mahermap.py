"""Main module."""
import random
import string

def generate_random_string(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


