# Program for Lexical Analysis
def printline():
    for i in range(80):
        print("=",end="")
    print()
import tokenize
t=[]
print("*** Ex5-Lexical Analysis ***")
printline()
a=input("Enter the file name:")
with open(a)as f:
    tokens=tokenize.generate_tokens(f.readline)
    for token in tokens:
        t.append(token)
print("The given Input is:",tokenize.untokenize(t))
g=(len(t))
print("*** The Tokens are ***")
print("Token\t\t\tName\t\tType")
printline()
for x in t:
    print("{:20s} {:10s} {:10d}".format(repr(x[1]),tokenize.tok_name[x[0]],x[0]))
printline()
print("Total No. of Tokens are:",g)
