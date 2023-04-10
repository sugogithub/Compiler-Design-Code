n=int(input("Enter no.of production rules:"))
g={}
first={}
print("Note:Use equal to (=) for production rules\n Specify | between Alternates)")
print("Enter ",n," Production rules one be one")
for i in range(n):
    t=input("Enter rule"+str(i+1)+":")
    g[t.split('=')[0]]=t.split('=')[1]
print(g)

def alternates(NT):
    x=g[NT].split("|")
    return x
               
# to check NonTerminals
def isNonTerminal(symbol):
    if symbol.isupper():
        return True
    else:
        return False
# to check Terminals
def isTerminal(symbol):
    if not symbol.isupper():
        return True
    else:
        return False

def alternatesFirst(NT):
    #af={}
    t=[]
    AL=alternates(NT)
    for L in AL:
        t.append(L[0])
    #af[NT]=set(t)
    return t

def nextSymbol(NT):
    t=[]
    for x in list(g.values()):
        loc=x.find(NT)
        if loc<len(x)-1 and NT in x:
            if x[loc+1]!='|':
                t.append(x[loc+1])
    return t
  
def FIRST(NT):
    F1=[]
    al=alternatesFirst(NT)
    for x in al:
        ns=nextSymbol(NT)
        if isNonTerminal(x):
            F1.extend(FIRST(x))
        elif isTerminal(x) and x!='e':
            F1.extend(x)
        elif isTerminal(x) and x=='e' and len(ns)>0:
            for y in ns:
                if isNonTerminal(y):
                    F1.extend(FIRST(y))
                else:
                    F1.extend(y)
        else:
            F1.extend(x)
                
    return F1

AF={}
for P in list(g.keys()):
    AF[P]=FIRST(P)
print("All First for the given Grammar")
for f in AF:
    print("First(",f,")->",AF[f])      

def isStartSymbol(NT):
    p=list(g.keys())
    if NT==p[0]:
        return True
    else:
        return False

def pStartSymbol(NT):
    t=[]
    for x in list(g.keys()):
        if NT in g[x]:
            t.extend(x)
    return t
    
def FOLLOW(NT):
    t=[]
    ns=nextSymbol(NT)
    if isStartSymbol(NT):
        t.extend('$')
    if len(ns)>0:
        for nx in ns:
            if isNonTerminal(nx):
                for x in FIRST(nx):
                    if x=='e':
                        t.extend(FOLLOW(nx))
                    else:
                        t.extend(x)
            else:
                t.extend(nx)#if Terminal
    else:
        a=pStartSymbol(NT)
        if len(a)>0:
            for x in a:
                if x!=NT:
                    t.extend(FOLLOW(x))
    return t
                    
FW={}
for a in list(g.keys()):
    FW[a]=set(FOLLOW(a))
    
print("All Follow for the given Grammar")
for f in FW:
    print("First(",f,")->",FW[f])
