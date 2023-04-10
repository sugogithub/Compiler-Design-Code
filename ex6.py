"""
Grammar
E=TE'
E'=+TE'|e
T=FT'
T'=*FT'|e
F=id|(E)
"""
import re
# Prediction Table
M={("E","id"):"T,EE",("E","("):"T,EE",
   ("EE","+"):"+,T,EE",("EE",")"):"e",("EE","$"):"e",
   ("T","id"):"F,TT",("T","("):"F,TT",
   ("TT","+"):"e",("TT","*"):"*,F,TT",("TT",")"):"e",("TT","$"):"e",
   ("F","id"):"id",("F","("):"(,E,)",
   }
S=["$","E"]# Stack with Start Symbol
#iw="(id)$"
iw=input("Enter valid Input String for Predictive Parsing:")
if iw[-1]!="$":
    print("Input Must Ends with $")
    exit()
    
def tokens(iw):
    iwl = re.findall(r"[a-zA-Z_]\w*|[+\-*\/()]|\S", iw)
    return iwl

def stacktop(stack):
    return stack[-1]
def push(stack,value):
    stack.extend(value[::-1])
def pop(stack):
    stack.pop()

def show(stack,inputword,action):
    #{:20s} {:10s} {:10d}
    a=str(stack).replace("'","")
    b=str(inputword).replace("'","")
    c=str(action).replace("'","")
    print("{:15s}\t{:15s}\t{:15s}".format(a,b,c))

def predict(stack,inputword):
    try:
        grammar=(str(M[(stack[-1],inputword[0])])).split(",")
    except KeyError:
        return "Error" 
    return grammar

def parse(stack,inputword):
    if stacktop(stack)=="$" and inputword[0]=="$":
        show(stack,inputword,"Accepted")
        exit()
    elif stacktop(stack)==inputword[0]:
        show(stack,inputword,"Match")
        pop(stack)
        inputword.pop(0)
    else:
        r=predict(stack,inputword)
        show(stack,inputword,r) #predicted Production
        if r=="Error":
            print("Error")
            exit()
        else:
            pop(stack)
            push(stack,r)
        if stacktop(stack)=='e':
            pop(stack)
    parse(stack,inputword)
iwl=tokens(iw)
print("Given Input word is:",iwl)
print("======================================================================")
print("{:15s}\t{:15s}\t{:15s}".format("Stack","InputBuffer","Grammar/Action"))
print("======================================================================")
parse(S,iwl)



