import collections



def hashable(inputt, unhashable):
    try:
        hash(inputt)
    except TypeError:
        print("Not possible!")
        unhashable['unhashable'] = True
        return False
    return True



if __name__=="__main__":
    inputt = {'a': (1, 2, [3]), 'b': 'c'}
    print ("Input:",inputt)
    value=0
    key=0
    unhashable = {'unhashable': False}
    output={value:key
            for key, value in inputt.items()
            if hashable(value, unhashable)}
    if not unhashable['unhashable']:
        print ("Output:", output)
       




