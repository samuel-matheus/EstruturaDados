from random import shuffle

def bogosort(seq):
    como_deve_ficar = sorted(seq)
    while seq != como_deve_ficar:
        shuffle(seq)
