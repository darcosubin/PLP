'''Merging two dictionaries'''
from collections import OrderedDict

def merge(first_dict, second_dict, new_dict):
    """This will merge the two dictionfirst_dictries"""
    unique = True
    keys_in_both_lists = conc(first_dict, second_dict, unique)
    for key in keys_in_both_lists:
        if first_dict.get(key) is None:
            new_dict[key] = second_dict.get(key)
            print "Not found:", key
        elif second_dict.get(key) is None:
            new_dict[key] = first_dict.get(key)
            print "Not found:", key
        elif not isinstance(first_dict[key], type(second_dict[key])):
            new_dict[key] = (first_dict[key], {second_dict[key]})
        elif isinstance(first_dict[key], list):
            new_dict[key] = conc(first_dict[key],
                                 second_dict[key],
                                 unique=False)
        elif isinstance(first_dict[key], set):
            new_dict[key] = first_dict[key] | second_dict[key]
        elif isinstance(first_dict[key], dict):
            new_dict[key] = merge(first_dict[key],
                                  second_dict[key],
                                  {})
        else:
            new_dict[key] = first_dict[key] + second_dict[key]
    return OrderedDict(sorted(new_dict.items()))


def conc(list_a, list_b, unique):
    """This will concatenate the two given lists"""
    flattened = []
    for element_i in [list_a, list_b]:
        for element_in_i in element_i:
            if element_in_i not in flattened and unique is True:
                flattened.append(element_in_i)
            else:
                flattened.append(element_in_i)
    return flattened


def test_merge():
    '''It will test if the merge works'''
    assert merge({'1': 2}, {'1': 3}, {}) == {'1': 5}


def test_sets():
    '''It will test if the merge for sets works'''
    assert merge({'q': set([7, 8, 9])},
                 {'q': 'abcd'},
                 {}) == {'q': (set([7, 8, 9]),
                               set(['abcd']))}


def test_1stfull():
    '''It will test if the merge for 1st full works'''
    assert merge({'a': 2}, {}, {}) == {'a': 2}


def test_1stempty():
    '''It will test if the merge for 1st empty works'''
    assert merge({}, {'a': 2}, {}) == {'a': 2}


if __name__ == "__main__":
    FIRST_DICT = {'x': [1, 2, 3],
                  'y': 1,
                  'z': set([1, 2, 3]),
                  'w': 'qweqwe',
                  't': {'a': [1, 2]},
                  'm': [1],
                  'q': 'xzz'}
    SECOND_DICT = {'x': [4, 5, 6],
                   'y': 4,
                   'z': set([4, 2, 3]),
                   'w': 'asdf',
                   't': {'a': [3, 2]},
                   'm': "wer",
                   'n': 'x'}
    NEW_DICT = {}
    MERGED = (merge(FIRST_DICT, SECOND_DICT, NEW_DICT))
    print MERGED