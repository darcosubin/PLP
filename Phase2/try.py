feed=0

def foo():
    global feed
    feed=10
    print feed

def fof():
    feed+=2
    print feed

if __name__=="__main__":
    foo()
   # fof()