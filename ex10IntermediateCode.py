import re

def tokens(iw):
    iwl = re.findall(r"[a-zA-Z_]\w*|[+\-*\/()]|\S", iw)
    return iwl

def getexp(op,exp):
    e = tokens(exp)
    for i in range(len(e)):
       if e[i]==op:
            return list(e[i-1]+e[i]+e[i+1])
    
def getop(exp):
    opt=[]
    op=['/','*','+','-']
    ops = re.findall(r"[()/*+-]", exp)
    for x in op:
        for y in ops:
            if x==y:
                opt.append(x)
    return opt
def listToString(L):
    s=''
    for x in L:
        s=s+x
    return s
        
temp={}
def gen_ic(exp):
    i=1
    op=getop(exp)
    for x in op:
        if '/'in x:
            temp['t'+str(i)]=getexp('/',exp)
        if '*'in x:
            temp['t'+str(i)]=getexp('*',exp)
        if '+'in x:
            temp['t'+str(i)]=getexp('+',exp)
        if '-'in x:
            temp['t'+str(i)]=getexp('-',exp)
        exp=exp.replace(listToString(temp['t'+str(i)]),'t'+str(i))
        i=i+1
    return temp
        
e=input("Enter any expression:")
a=e.split("=")[1]
print("Given Expression:",e)
tac=gen_ic(a)
for x in tac:
    print(x,"=",listToString(tac[x]))
print(e.split("=")[0],"=",x)
            
    

