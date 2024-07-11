#Writing into a file till user wants
def fileout(n):
    f=open(n,'w')
    while True:
        c=input("Enter the line to be added or 'q' to quit ")
        if c!='q':
            f.write(c)
            f.write("\n")
        else:
            break
fileout(“user.txt")
