#Fibonacci
a=0
b=1
n=int(input("How many terms do you want  in the series :"))
print("Fibonacci Series :")
print("0")
print("1")

for i in range(n-2):
    c=a+b
    a,b=b,c
    print( c)
