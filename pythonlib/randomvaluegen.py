import random
import string

def generatename():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(20))

def generateid():
    return "".join(random.choice(string.digits) for _ in range(10))

