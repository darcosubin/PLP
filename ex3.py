entry=" "
str1=" "
str2=0
x=0
def readfromfile():
    with open ("inf.txt", 'r') as iff:
        entry=iff.readlines()
    return entry

def conc(list_a, list_b):
    """This will concatenate the two given lists"""
    flattened = []
    for element_i in [list_a, list_b]:
        for element_in_i in element_i:
            flattened.append(element_in_i)
    return flattened

def splitndict():
    variablesRead=readfromfile()
    splitted=[i.split() for i in variablesRead]
    d={}
    for lines in splitted:
        if lines=="\n":
            splines=lines.split()
        for line in splines:
            line=conc(lines[0],lines[1])
            d[line[0]]=int(line[1])
            print d
    return d


def writeinfile():
    with open ("ouf.txt", 'w') as off:
        off.write(str(splitndict()))


if __name__ == "__main__":
    readfromfile()
    writeinfile()
    splitndict()