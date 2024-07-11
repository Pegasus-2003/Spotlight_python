# Displaying words less than 4 character
def display_words(n):
    m=[]
    f=open(n,'r')
    s=f.read()
    g=s.split()
    for i in g:
        if len(i)<4:
            m.append(i)
    print(m)

n=input("Enter the file to be read ")
display_words(n)

