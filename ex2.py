import tokenize
t=[]
i=0
op=0
j=0
a=input("enter the file name:")
with tokenize.open(a)as f:
    tokens=tokenize.generate_tokens(f.readline)
    for token in tokens:
        t.append(token)
f2=open(a)
print("The given Input is:",f2.read())
f2.close()
g=(len(t))
print("*** The Tokens are ***")
for x in t:
    if x[0]==1:
        print('Name or Identitifier:',x[1])
        i=i+1
    elif x[0]==2:
        print("the values:",x[1])
        j=j+1
    elif x[0]==4:
        print('Newline :','\\n')
    elif x[0]==54:
        print('Operator:','->',x[1])
        op=op+1
    else:
        print("End of the Code",x[0])
print("the total number of tokens:",g-1)
print("mumber of identifires:",i)
print("the number of operators:",op)
print("the number of values:",j)
