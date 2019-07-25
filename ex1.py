import unittest

class TestFlatten(unittest.TestCase):

    def test_flattendepth1(self):
        self.assertEqual(
            flatten(
                [1,2,3],
                [4,5],2),
            [1,2,3,4,5]
            )




def conc(list_a,list_b):

    flattened=[]
    for i in [list_a,list_b]:
        for x in i:
            flattened.append(x)
    return flattened

def flatten(list_a,list_b,max_depth):
    q=[]
    for i in conc(list_a,list_b):
        if type(i)==list:
            newI=flatten(i,[],max_depth)
            for j in newI:
                q.append(j)
        else:
            q.append(i)
    return q



if __name__ == "__main__":
    a=[1,2,7,3,[4,5]]
    b=['a','b','c',['d',['e','f']]]
    c=2
    print (conc(a,b))
    print (flatten(a,b,c))
    #unittest.main()


