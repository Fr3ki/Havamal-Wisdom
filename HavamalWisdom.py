import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

def Stanza(Havamal):
    lines = open(Havamal).read().splitlines()
    return random.choice(lines)
print(Stanza('Havamal'))
