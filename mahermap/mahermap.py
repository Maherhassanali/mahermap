"""Main module."""
import random
import string

def generate_random_string(length=5):
    letters = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

def the_name(name):
    print(name)
