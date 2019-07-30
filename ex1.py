import unittest

class TestFlatten(unittest.TestCase):

    def test_flattendepth1(self):
        self.assertEemptyListual(
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
    emptyList=[]
    for i in conc(list_a,list_b):
        if type(i)==list:
            newI=flatten(i,[],max_depth)
            for j in newI:
                emptyList.append(j)
        else:
            emptyList.append(i)
    return emptyList

def depth(list_a,list_b,max_depth):
    max_depth=int(input("Enter the depth you wish: "))
    emptyList=[]
    p=0
    for i in conc(list_a,list_b):
        if type(i)==list:
            newI=flatten(i,[],max_depth)
            p+=1
            if p>=max_depth:
                pass
            else:
                for j in newI:
                    emptyList.append(j)
        else:
            emptyList.append(i)
    return emptyList


if __name__ == "__main__":
    a=[1,2,7,3,[4,[5]]]
    b=['a','b','c',['d',['e',['f']]]]
    c=0
    print (conc(a,b))
    print (flatten(a,b,c))
    print (depth(a,b,c))
    #unittest.main()


