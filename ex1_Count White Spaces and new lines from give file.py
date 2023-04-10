print("*** Ex1 - Count White spaces and Number of Lines ***")
fname=input("Enter the File name to Process:")
try:
    file=open(fname)
    lines = 0
    spaces = 0
    print("The File Content is")
    print("*******************")
    content=file.read()
    print(content)
    f1=open(fname)
    for line in f1:
        lines += 1
        for char in line:
            if char == ' ':
                spaces += 1
    print("************************")
    print("Number of lines:", lines)
    print("Number of spaces:", spaces)
except FileNotFoundError:
    print("The given",fname," file is not exist!")
