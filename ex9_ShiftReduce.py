"""
Grammar
E=E+E 
E=E*E
E=(E)
E=id
"""
import re
# Grammar
G={'E':'E+E|E*E|(E)|id'}
S=["$"]# Stack with Start and follow Symbol
#iw="(id)$"
iw=input("Enter valid Input String for Shift-Reduce Parsing:")
if iw[-1]!="$":
    print("Input Must Ends with $")
    exit()
    
def tokens(iw):
    iwl = re.findall(r"[a-zA-Z_]\w*|[+\-*\/()]|\S", iw)
    return iwl

def stackTop(stack):
    return stack[-1]

def listToString(L):
    s=""
    for x in L:
        s=s+x
    return s
    
def shift(stack,inputword):
    if len(inputword)>0:
        stack.append(inputword[0])
        inputword.remove(inputword[0])
    return "Shift"
        
def startSymbol(G):
    g=list(G.keys())
    return g[0]

def handle(stack):
    for x in G['E'].split("|"):
        if stackTop(stack)==x:
            stack.pop()
            stack.extend('E')
            return 'E='+x
def reduce(stack):
    for x in G['E'].split("|"):
        if listToString(stack[len(stack)-3:])==x:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.extend('E')
            return ("Reduce by E="+x)
       
def show(stack,inputword,action):
    #{:20s} {:10s} {:10d}
    a=str(stack).replace("'","")
    b=str(inputword).replace("'","")
    c=str(action).replace("'","")
    print("{:15s}\t{:25s}\t{:15s}".format(a,b,c))

def SRParse(stack,inputword):
    show(stack,inputword,shift(stack,inputword))
    show(stack,inputword,handle(stack))
    show(stack,inputword,reduce(stack))
    if len(stack)==2 and stackTop(stack)==startSymbol(G)and inputword[0]=='$':
        show(stack,inputword,'Accepted - Done')
    elif inputword[0]!='$':
        SRParse(stack,inputword)
    else:
        show(stack,inputword,'Not Accepted - Done')
            
iwl=tokens(iw)
print("Given Input word is:",iwl)
print("======================================================================")
print("{:15s}\t{:25s}\t{:15s}".format("Stack","InputBuffer","Action"))
print("======================================================================")
show(S,iwl,"Begins")
SRParse(S,iwl)



