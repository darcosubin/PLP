entry=" "
str1=" "
str2=0
x=0
def readfromfile():
    with open ("inf.txt", 'r') as iff:
        entry=iff.readlines()
    return entry



def splitndict():
    variablesRead=readfromfile()
    splitted=[i.split() for i in variablesRead]
    for j in splitted:
        d={}
        d[j[0]]=int(j[1])
        print d
    print splitted
    return splitted


def writeinfile():
    with open ("ouf.txt", 'w') as off:
        off.write(str(splitndict()))


if __name__ == "__main__":
    readfromfile()
    writeinfile()
    splitndict()