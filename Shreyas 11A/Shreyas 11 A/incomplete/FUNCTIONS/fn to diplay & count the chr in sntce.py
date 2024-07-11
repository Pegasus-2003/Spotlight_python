def character(n):
    d={}
    for i in n:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    print(n,'=',len(n))
    print(d)

x=input("Enter a sentence: ")
character(x)
