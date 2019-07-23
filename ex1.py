import unittest

class TestFlatten(unittest.TestCase):

    def test_flattendepth1(self):
        self.assertEqual(
            flatten(
                [1,2,3],
                [4,5],2),
            [1,2,3,4,5]
            )

def flatten(list_a,list_b,max_depth):
    pass
if __name__ == "__main__":
    unittest.main()