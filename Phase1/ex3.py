'''Sorting two dictionaries by their keys'''


def readfromfile():
    '''Reading from file'''
    with open("inf.txt", 'r') as iff:
        entry = iff.readlines()
    return entry


def enum():
    '''Enumerating'''
    listofj = []
    listen = list(enumerate(splitndict(), start=1))
    for index in listen:
        for jndex in index:
            listofj.append(jndex)
            break
    print listofj
    return listofj


def splitndict():
    '''Splitting and making a dict'''
    listofd = []
    variablesread = readfromfile()
    splitted = [i.split() for i in variablesread]
    newdict = {}
    for lines in splitted:
        if lines:
            newdict[lines[0]] = int(lines[1])
        elif newdict == {}:
            pass
        else:
            listofd.append(newdict)
            newdict = {}
    listen = list(enumerate(listofd, start=1))
    print listen
    return listen


def sortdicts():
    '''Sorting the dicts'''
    listofs = []
    listofs = splitndict()
    sorteds = sorted(listofs, key=lambda items: min(items[1].values()))
    print ([
        i[0]
        for i in sorteds
    ])
    return sorteds


def writeinfile():
    '''Writing in file'''
    sortedd = sortdicts()
    ind = [
        iterator[0]
        for iterator in sortedd
    ]
    inx = [
        jterator[1]
        for jterator in sortedd
    ]
    with open("ouf.txt", 'w') as off:
        off.write("Sorted dictionaries by vaule from keys are: ")
        off.write("\n")
        off.write(str(inx))
        off.write("\n\n")
        off.write("Sorted index of dictionaries are: ")
        off.write("\n")
        off.write(str(ind))


if __name__ == "__main__":
    writeinfile()
    sortdicts()
