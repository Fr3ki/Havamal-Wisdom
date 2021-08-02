import random
import cowsay

def Stanza(Havamal):
    lines = open(Havamal).read().splitlines()
    return random.choice(lines)
cowsay.cow(Stanza('Havamal'))
