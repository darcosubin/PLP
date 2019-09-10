'''Swapping key <-> values of a dictionary'''


def hashable(inp):
    '''Swapping using try/except and hash'''
    try:
        hash(inp)
    except TypeError:
        print "Not possible!"
        return False
    return True


class TheHash(object):
    "implement simple custom objectto check if it's hashable"
    def __init__(self, objects):
        """hold a simple integer to check that objects
            with same value are still different"""
        self.objects = objects


def hashable1(walue):
    '''Swapping without using try/except and hash'''
    if isinstance(walue, tuple):
        for items in walue:
            if not hashable1(items):
                UNHASHABLE['unhashable'] = True
                return False
        return True
    if hashable2(walue):
        return True
    UNHASHABLE['unhashable'] = True
    return False


def hashable2(obj):
    '''Checking if any object is hashable'''
    if hasattr(obj, '__hash__') and (callable(obj.__hash__)):
        return True
    return False


if __name__ == "__main__":
    INPUT = {'a': 123, 'b': (1, 2, 3), 'c': TheHash(4)}
    print ("Input:", INPUT)
    OUTPUT = 0
    UNHASHABLE = {'unhashable': False}
    for key, value in INPUT.items():
        if not hashable1(value):
            print ("Output: ", "Impossible!")
            break
    if not UNHASHABLE['unhashable']:
        OUTPUT = {value: key
                  for key, value in INPUT.items()}
        print ("Output:", OUTPUT)
