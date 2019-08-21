def readfromfile():
    with open ("inf.txt", 'r') as iff:
        entry=iff.readlines()
    return entry


def splitndict():
    listofd=[]
    variablesRead=readfromfile()
    splitted=[i.split() for i in variablesRead]
    d={}
    for lines in splitted:
        if lines:
            d[lines[0]]=int(lines[1])
        elif d=={}:
            pass
        else:
            listofd.append(d)
            d={}
        print listofd
    return listofd


def sortdicts():
    listofs=[]
    listofs=splitndict()
    for item in listofs:
        item=sorted(listofs, key=lambda d: min(d.keys()))
        print item


def writeinfile():
    with open ("ouf.txt", 'w') as off:
        off.write(str(splitndict()))


if __name__ == "__main__":

    writeinfile()
    sortdicts()