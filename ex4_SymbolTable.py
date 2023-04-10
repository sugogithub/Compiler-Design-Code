import symtable
print("*** Ex4 - Symbol table Creation ***")
fn=input("Enter the Input filename:")
f=open(fn)
code=str(f.read())
print(code)
symt = symtable.symtable(code,fn, "exec")
print("Identifiers")
for ident in symt.get_identifiers():
    print(ident)
print("Symbol Table Created!...")
se=input("Enter Identifier to lookup:")
try:
    if symt.lookup(se):
        print(se, " is in Symbol Table")
except KeyError:
    print(se," is NOT in Symbol Table")




                    
                    
                    

