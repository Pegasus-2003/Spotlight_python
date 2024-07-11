# Fileout and append till user wants
class fileout():
    def write(self):
        h='n'
        f=open("nice2.txt",'w')
        i=""
        while i!=h:
            i = input("Enter after each line and type 'n' to stop ")
            if i!=h:
                f.write(i+'\n')


h=fileout()
h.write()
