#Words that strt and end with same letter
def wordcount(l):
    f=open(l,'r')
    s=f.read()
    l=s.split()
    for i in l:
        if i[0]==i[-1]:
            print(i)
wordcount(“ARTICLE.txt")
