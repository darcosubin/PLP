import unittest
import types


class TestFlatten(unittest.TestCase):
    def test_flattendepth1(self):
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=1,
                currentDepth=0
            ),
            [1, 2, 7, 3, 'a', 'b', 'c'],
            )


class TestFlatten2(unittest.TestCase):

    def test_flattendepth2(self):
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=2,
                currentDepth=0
            ),
            [1, 2, 7, 3, 4, 'a', 'b', 'c', 'd'],
            )


class TestFlatten3(unittest.TestCase):

    def test_flattendepth3(self):
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=3,
                currentDepth=0
            ),
            [1, 2, 7, 3, 4, 5, 'a', 'b', 'c', 'd', 'e'],
            )


class TestFlatten4(unittest.TestCase):

    def test_flattendepth4(self):
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=4,
                currentDepth=0
            ),
            [1, 2, 7, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f'],
            )


def conc(list_a, list_b):
    flattened = []
    for elementI in [list_a, list_b]:
        for elementinI in elementI:
            flattened.append(elementinI)
    return flattened


def flatten(list_a, list_b, max_depth, currentDepth):
    emptyList = []
    for elementI in conc(list_a, list_b):
        if isinstance(elementI, (tuple, list)):
            currentDepth += 1
            newI = flatten(elementI, [], max_depth, currentDepth)
            if currentDepth < max_depth:
                for elemInI in newI:
                    emptyList.append(elemInI)
                currentDepth -= 1
        else:
            emptyList.append(elementI)
    return emptyList


if __name__ == "__main__":
    list_a = [1, 2, 7, 3, [4, [5, [6]]]]
    list_b = ['a', 'b', 'c', ['d', ['e', ['f']]]]
    max_depth = 0
    currentDepth = 0
    print(conc(list_a, list_b))
    max_depth = int(input("Enter the depth you wish: "))
    print(flatten(list_a, list_b, max_depth, currentDepth))
    unittest.main()
