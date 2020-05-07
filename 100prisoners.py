# From https://rosettacode.org/wiki/100_prisoners#Python

import random
from sys import argv 

def play_random(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 0
    in_drawer = list(range(100))
    sampler = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        found = False
        for prisoner in range(100):
            found = False
            for reveal in random.sample(sampler, 50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %
 
def play_optimal(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 0
    in_drawer = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        for prisoner in range(100):
            reveal = prisoner
            found = False
            for go in range(50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
                reveal = card
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %
 
if __name__ == '__main__':
    n = int(argv[1])
    print("Simulation count:", n)
    r = play_random(n)
    o = play_optimal(n)
    print("Random play wins: ", r, "% of simulations")
    print("Optimal play wins: ", o, "% of simulations")
