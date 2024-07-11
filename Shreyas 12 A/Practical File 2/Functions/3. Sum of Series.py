# Sum of the series       "1!/1+2!/2+3!/3+4!/4+5!/5 "
def fact(x):
    p=1
    for i in range (1,x+1):
        p=i*p
    a=p/x
    return a
S=0
for i in range(1,6):
    S+=fact(i)
print("1!/1+2!/2+3!/3+4!/4+5!/5 =",S)
