def spaces(n):
    a=0
    for i in range(0,len(n)):
        if n[i]==' ':
            a+=1
    print(a)

x=input("Enter a sentence: ")
spaces(x)
