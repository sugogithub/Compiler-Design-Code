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
  
def FIRST1(NT):
    F1=[]
    al=alternatesFirst(NT)
    for x in al:
        ns=nextSymbol(NT)
        if isNonTerminal(x):
            F1.extend(FIRST1(x))
        elif isTerminal(x) and x!='e':
            F1.extend(x)
        elif isTerminal(x) and x=='e' and len(ns)>0:
            for y in ns:
                if isNonTerminal(y):
                    F1.extend(FIRST1(y))
                else:
                    F1.extend(y)
        else:
            F1.extend(x)
                
    return F1

AF={}
for P in list(g.keys()):
    AF[P]=FIRST1(P)
print("All First for the given Grammar")
for f in AF:
    print("First(",f,")->",AF[f])      

    
