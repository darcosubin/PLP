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

def depth(list_a,list_b,max_depth):
    max_depth=int(input("Enter the depth you wish: "))
    q=[]
    p=0
    for i in conc(list_a,list_b):
        if type(i)==list:
            newI=flatten(i,[],max_depth)
            p+=1
            if p>=max_depth:
                pass
                for i in newI:
                    if type(i)==list:
                        newP=flatten(i,[],max_depth)
                        for j in newP:
                            q.append(j)
            else:
                for j in newI:
                    q.append(j)
        else:
            q.append(i)
    return q


if __name__ == "__main__":
    a=[1,2,7,3,[4,5]]
    b=['a','b','c',['d',['e',['f']]]]
    c=1
    print (conc(a,b))
    print (flatten(a,b,c))
    print (depth(a,b,c))
    #unittest.main()


