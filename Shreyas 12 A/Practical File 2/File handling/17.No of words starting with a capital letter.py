#No of words starting with a capital letter
def count(l):
    f=open(l,'r')
    s=f.read()
    l=s.split()
    c=0
    for i in l:
        if i[0].isupper():
            c+=1
    print("NUMBER OF UPPER CASE ",c)
count("coordinate.txt") 
