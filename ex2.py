'''Merging two dictionaries'''

def merge(first_dict, second_dict, new_dict):
    """This will merge the two dictionaries"""
    for key in first_dict.keys():
        if second_dict.get(key) is None:
            print "Not found:",key
            new_dict[key]=first_dict[key]
        elif not isinstance(first_dict[key], type(second_dict[key])):
            new_dict[key] = (first_dict[key], second_dict[key])
        elif isinstance(first_dict[key], list):
            new_dict[key] = conc(first_dict[key], second_dict[key])
        elif isinstance(first_dict[key], set):
            new_dict[key] = first_dict[key] | second_dict[key]
        elif isinstance(first_dict[key], dict):
            new_dict[key] = merge(first_dict[key], second_dict[key], {})
        else:
            new_dict[key] = first_dict[key] + second_dict[key]
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
    assert merge({'q':set([7, 8, 9])}, {'q':'abcd'}, {}) == {'q': (set([7, 8, 9]), 'abcd')}
    assert merge({'a':2}, {}, {}) == {'a':2}
    assert merge({}, {'a':2}, {}) == {'a':2}


if __name__ == "__main__":
    FIRST_DICT = {'x': [1, 2, 3],
                  'y': 1,
                  'z': set([1, 2, 3]),
                  'w': 'qweqwe',
                  't': {'a': [1, 2]},
                  'm': [1]}
    SECOND_DICT = {'x': [4, 5, 6],
                   'y': 4,
                   'z': set([4, 2, 3]),
                   'n': 'abc',
                   'w': 'asdf',
                   't': {'a': [3, 2]},
                   'm': "wer"
                   }
    NEW_DICT = {}
    MERGED = (merge(FIRST_DICT, SECOND_DICT, NEW_DICT))
    print MERGED
