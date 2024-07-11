#No of A's and E's
def count(l):
    f=open(l,'r')
    s=f.read()
    c1=0
    c2=0
    l1=['A','a']
    l2=['E','e']
    for i in s:
        if i in l1:
            c1+=1
        elif i in l2:
            c2+=1
    print("Number of A's =",c1)
    print("Number of E's =",c2)
count("Poem.txt")
