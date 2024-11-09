import sys

niz = sys.stdin.readline().strip()
string = ""

def S():
    global string, niz
    string = string + "S"
    if len(niz) > 0 and niz[0] == "a":
        niz = niz[1:]
        A()
        B()
    elif len(niz) > 0 and niz[0] == "b":
        niz = niz[1:]
        B()
        A()
    else:
        print(string + "\n" + "NE")
        exit()

def A():
    global string, niz
    string = string + "A"
    if len(niz) > 0 and niz[0] == "b":
        niz = niz[1:]
        C()
    elif len(niz) > 0 and niz[0] == "a":
        niz = niz[1:]
    else:
        print(string + "\n" + "NE")
        exit()
def B():
    global string, niz
    string = string + "B"
    if(len(niz) > 1 and niz[0] == "c" and niz[1] == "c"):
        niz = niz[2:]
        S()
    if(len(niz) > 1 and niz[0] == "b" and niz[1] == "c"):
        niz = niz[2:]

def C():
    global string, niz
    string = string + "C"
    A()
    A()

S()

if(len(niz) > 0):
    print(string + "\n" + "NE")
else:
    print(string + "\n" + "DA")