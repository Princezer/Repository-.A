""" The token generator
it will select a token and stuff
"""

import random

Tokens = ["Unicorn", "Donkey", "Donkey", "Horse", "Horse", "Zebra", "Zebra"]

for item in range (1):
    Token = random.choice(Tokens)
print (Token, end = "\t")