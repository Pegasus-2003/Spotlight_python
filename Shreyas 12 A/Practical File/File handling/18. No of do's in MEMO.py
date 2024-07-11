# No of do's in MEMO
def count(l):
    f=open(l)
    s=f.read()
    l=s.split()
    c=0
    l1=["DO","do"]
    for i in l:
        if i in l1:
            c+=1
    print(c)
count("MEMO.TXT") 
