import random
import string

def getRandomValidEmail(stringLength=10):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    s= ''.join(random.choice(letters) for i in range(stringLength))
    valid_email=s+"@iovision.tn"
    return valid_email