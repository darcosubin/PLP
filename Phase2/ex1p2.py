'''Swapping key <-> values of a dictionary'''


def hashable(inp):
    '''Swapping using try/except and hash'''
    try:
        hash(inp)
    except TypeError:
        print "Not possible!"
        return False
    return True


def hashable1(value):
    '''Swapping without using try/except and hash'''
    if isinstance(value, tuple):
        for items in value:
            if not hashable1(items):
                UNHASHABLE['unhashable'] = True
                return False
        return True
    elif isinstance(value, int):
        return True
    elif isinstance(value, str):
        return True
    UNHASHABLE['unhashable'] = True
    return False


if __name__ == "__main__":
    INPUT = {'a': 123, 'b': (1, 2, [3])}
    print ("Input:", INPUT)
    OUTPUT = 0
    UNHASHABLE = {'unhashable': False}
    for key, value in INPUT.items():
        if not hashable1(value):
            print ("Output: ", "Impossible!")
    if not UNHASHABLE['unhashable']:
        OUTPUT = {value: key
                  for key, value in INPUT.items()}
        print ("Output:", OUTPUT)
