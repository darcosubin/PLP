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
    c=conc(list_a,list_b)
    elist=[]
    for i in list_a:
        if type(i)==list:
            newI=flatten(i,[],max_depth)
            if newI is not None:
                for j in newI:
                    elist.append(j)
            else:
                elist.append(i)
    return elist


def conc(list_a,list_b):

    flattened=[]
    for i in [list_a,list_b]:
        for x in i:
            flattened.append(x)
    return flattened



if __name__ == "__main__":
    print conc([1,2,3,[4,5]],['a','b','c','d',['e']])
    a=[1,2,7,3,[4,5]] 
    b=[1,2,[3,[4,5]]]
    c=2
    print flatten(a,b,c)
    #unittest.main()


