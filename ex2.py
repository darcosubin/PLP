'''Merging two dictionaries'''

def merge(first_dict, second_dict, new_dict):
    """This will merge the two dictionfirst_dictries"""
    for key in first_dict.keys():
        if not isinstance(first_dict[key], type(second_dict[key])):
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
    """This will concfirst_dicttenate the two given lists"""
    flattened = []
    for element_i in [list_a, list_b]:
        for element_in_i in element_i:
            flattened.append(element_in_i)
    return flattened


def test_merge():
    '''It will test if the merge works'''
    assert merge({'1':2}, {'1':3}, {}) == {'1':5}


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
                   'w': 'asdf',
                   't': {'a': [3, 2]},
                   'm': "wer"}
    MERGED = (merge(FIRST_DICT, SECOND_DICT, {}))
    print MERGED
