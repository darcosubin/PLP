import unittest
import types


class TestFlatten(unittest.TestCase):
    def test_flattendepth1(self):
        self.assertEqual(
            flatten(
                list_a=[1, 2, 7, 3, [4, [5, [6]]]],
                list_b=['a', 'b', 'c', ['d', ['e', ['f']]]],
                max_depth=1,
                p=0
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
                p=0
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
                p=0
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
                p=0
            ),
            [1, 2, 7, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f'],
            )


def conc(list_a, list_b):
    flattened = []
    for i in [list_a, list_b]:
        for x in i:
            flattened.append(x)
    return flattened


def flatten(list_a, list_b, max_depth, p):
    emptyList = []
    for i in conc(list_a, list_b):
        if isinstance(i, (tuple, list)):
            p + = 1
            newI = flatten(i, [], max_depth, p)
            if p < max_depth:
                for j in newI:
                    emptyList.append(j)
                p - = 1
        else:
            emptyList.append(i)
    return emptyList


if __name__ == "__main__":
    list_a = [1, 2, 7, 3, [4, [5, [6]]]]
    list_b = ['a', 'b', 'c', ['d', ['e', ['f']]]]
    max_depth = 0
    p = 0
    print(conc(list_a, list_b))
    max_depth = int(input("Enter the depth you wish: "))
    print(flatten(list_a, list_b, max_depth, p))
    unittest.main()
