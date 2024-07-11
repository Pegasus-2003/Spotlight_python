def words(n):
    a=0
    for i in range(0,len(n)):
        if n[i]==' ':
            a+=1
    print(a+1)

x=input("Enter a sentence: ")
words(x)
