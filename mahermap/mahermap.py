"""Main module."""
import random
import string
import ipyleaflet



class Map(ipyleaflet.Map):


    def __init__(self) -> None:
        super().__init__()




def generate_random_string(length=5):
    
    """
    Generate a random string of length 
    **enter the length of the string to generate the random string**

    Returns:
        string of length you entered
    """    
    letters = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

def the_name(name):
    """write the name

    Args:
        name (string): just write the name you want 
        for testing
    """    
    print(name)
