# Series.2 =  x -((x^2)/4) +((x^3)/9).......... ((x^n)/(n^2))
print("Sequence :   x -((x^2)/4) +((x^3)/9).......... ((x^n)/(n^2))")
x = int(input("Enter a term = "))
n=int(input("Till where you want the series :"))
sum=0
for i in range(1,n+1):
     a=(x**i)*((-1)**(i+1))/(i**2)
     sum+=a
print("Sum of the series :",sum)
