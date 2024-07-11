#No of uppercase in ARTICLE
def upper(n):
    f=open(n,'r')
    s=f.read()
    c=0
    for i in s:
        if i.isupper():
            c+=1
    return c
k=upper("Article.txt")
print("NO OF UPPERCASE =“,k)
