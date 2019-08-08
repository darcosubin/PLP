'''Merging two dictionaries'''
def merge(first_dict, second_dict, new_dict):
    """This will merge the two dictionaries"""
    for key1,key2 in zip(first_dict.keys(),second_dict.keys()):
        if second_dict.get(key1) is None:
            print "Not found:",key1, key2
            loop(second_dict,first_dict,new_dict)
            loop(first_dict,second_dict,new_dict)
        elif not isinstance(first_dict[key1], type(second_dict[key2])):
            new_dict[key1] = (first_dict[key1], second_dict[key2])
        elif isinstance(first_dict[key1], list):
            new_dict[key1] = conc(first_dict[key1], second_dict[key2])
        elif isinstance(first_dict[key1], set):
            new_dict[key1] = first_dict[key1] | second_dict[key2]
        elif isinstance(first_dict[key1], dict):
            new_dict[key1] = merge(first_dict[key1], second_dict[key2], {})
        else:
            new_dict[key1] = first_dict[key1] + second_dict[key2]
    return new_dict

def loop(first_dict, second_dict, new_dict):
    for key1,key2 in zip(first_dict.keys(),second_dict.keys()):
        if first_dict.get(key1) is None:
            new_dict[key2] = first_dict[key1]
            new_dict[key1] = first_dict[key2]
        elif not isinstance(first_dict[key1], type(second_dict[key2])):
            new_dict[key1] = (first_dict[key1], second_dict[key2])
        elif isinstance(first_dict[key1], list):
            new_dict[key1] = conc(first_dict[key1], second_dict[key2])
        elif isinstance(first_dict[key1], set):
            new_dict[key1] = first_dict[key1] | second_dict[key2]
        elif isinstance(first_dict[key1], dict):
            new_dict[key1] = merge(first_dict[key1], second_dict[key2], {})
        else:
            new_dict[key1] = first_dict[key1] + second_dict[key2]
    return new_dict


def conc(list_a, list_b):
    """This will concatenate the two given lists"""
    flattened = []
    for element_i in [list_a, list_b]:
        for element_in_i in element_i:
            flattened.append(element_in_i)
    return flattened


def test_merge():
    '''It will test if the merge works'''
    assert merge({'1':2}, {'1':3}, {}) == {'1':5}
def test_sets():
    assert merge({'q':set([7, 8, 9])}, {'q':'abcd'}, {}) == {'q': (set([7, 8, 9]), 'abcd')}
def test_1stfull():
    assert merge({'a':2}, {}, {}) == {'a':2}
def test_1stempty():
    assert merge({}, {'a':2}, {}) == {'a':2}


if __name__ == "__main__":
    FIRST_DICT = {'x': [1, 2, 3],
                  'y': 1,
                  'z': set([1, 2, 3]),
                  'w': 'qweqwe',
                  't': {'a': [1, 2]},
                  'm': [1],
                  'u': 'oh'
                  }
    SECOND_DICT = {'x': [4, 5, 6],
                   'y': 4,
                   'z': set([4, 2, 3]),
                   'w': 'asdf',
                   't': {'a': [3, 2]},
                   'm': "wer",
                   'n': 'abc'
                   }
    NEW_DICT = {}
    MERGED = (merge(FIRST_DICT, SECOND_DICT, NEW_DICT))
    print MERGED
