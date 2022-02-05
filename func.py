from random import randint
def time(t):

    for i in range(t):
        yield i


def randVals():
    priority = randint(-20, 19)

    length = randint(1, 100)

    return priority, length



