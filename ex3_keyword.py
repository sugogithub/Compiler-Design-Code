import keyword
def iskeyword(word):
    kwl=keyword.kwlist # Built-in list of Python Keywords
    if word in kwl:
        print("The Given word:\'",word,"\'is a Keyword")
    else:
        print("The Given word:\'",word,"\'is NOT a keyword")
print("*** Program to check whether given word is keyword or not ***")
wd=input("Enter a word to check:")
iskeyword(wd)

    
