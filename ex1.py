#!/usr/bin/env python
"""Flatten a list bi a given depth"""
import unittest


class TestFlatten(unittest.TestCase):
    """This will test flatten for given depths"""
    def test_flattendepth1(self):
        """This will test the flatten for depth1"""
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=1,
                current_depth=0
            ),
            [1, 2, 7, 3, 'a', 'b', 'c'],
            )

    def test_flattendepth2(self):
        """This will test the flatten for depth2"""
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=2,
                current_depth=0
            ),
            [1, 2, 7, 3, 4, 'a', 'b', 'c', 'd'],
            )

    def test_flattendepth3(self):
        """This will test the flatten for depth3"""
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=3,
                current_depth=0
            ),
            [1, 2, 7, 3, 4, 5, 'a', 'b', 'c', 'd', 'e'],
            )

    def test_flattendepth4(self):
        """This will test the flatten for depth4"""
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=4,
                current_depth=0
            ),
            [1, 2, 7, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f'],
            )


def conc(list_a, list_b):
    """This will concatenate the two given lists"""
    flattened = []
    for element_i in [list_a, list_b]:
        for element_in_i in element_i:
            flattened.append(element_in_i)
    return flattened


def flatten(list_a, list_b, max_depth, current_depth):
    """This will flatten the given litst by the given depth"""
    empty_list = []
    for element_i in conc(list_a, list_b):
        if isinstance(element_i, (tuple, list)):
            current_depth += 1
            new_i = flatten(element_i, [], max_depth, current_depth)
            if current_depth < max_depth:
                for elem_in_i in new_i:
                    empty_list.append(elem_in_i)
                current_depth -= 1
        else:
            empty_list.append(element_i)
    return empty_list


if __name__ == "__main__":
    LIST_A = [1, 2, 7, 3, [4, [5, [6]]]]
    LIST_B = ['a', 'b', 'c', ['d', ['e', ['f']]]]
    MAX_DEEP = 0
    CURRENT_DEEP = 0
    print conc(LIST_A, LIST_B)
    MAX_DEEP = int(input("Enter the depth you wish: "))
    print flatten(LIST_A, LIST_B, MAX_DEEP, CURRENT_DEEP)
    unittest.main()
