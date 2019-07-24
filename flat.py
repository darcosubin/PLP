def flatten(list_a,list_b,max_depth):
    list_a=[[1,2,3,[4,5]]] 
    list_b=[['a','b','c',['d',['e']]]]
    lists=[]
    lists=list_a+list_b
    print lists
    print list_a
    print list_b
    max_depth=1
    print max_depth
    flattennedList=[]
    for sublist in lists:
        for val in sublist:
            flattennedList.append(val)
    print flattennedList
flatten([1,2,3,[4,5]],['a','b',['c',['d','e']]],1)  