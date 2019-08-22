def readfromfile():
    with open ("inf.txt", 'r') as iff:
        entry=iff.readlines()
    return entry


def enum(listofj=[]):
    listofj=[]
    listen=list(enumerate(splitndict(), start=1))
    for index in listen:
        for jndex in index:
            listofj.append(jndex)
            break
    print listofj
    return listofj


def splitndict(listofd=[]):
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
    listofd=[]
    listofs=[]
    listofs=splitndict(listofd)
    sorteds=sorted(listofs, key=lambda items: min(items.values()))
    print sorteds
    return sorteds




def writeinfile():
    x=str(enum(sortdicts()))
    with open ("ouf.txt", 'w') as off:
        off.write(str(sortdicts()))
        off.write("\n\n")
        off.write(x)


if __name__ == "__main__":

    writeinfile()
    sortdicts()