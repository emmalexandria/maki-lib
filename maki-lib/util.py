import random

def gen_id() -> int:
    return random.randrange(1 << 30, 1 << 31)
    

