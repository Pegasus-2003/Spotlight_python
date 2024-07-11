# Series.1 =  (1^2) + (2^2) + (3^2)...................(n^2)
print("Sequence : (1^2) + (2^2) + (3^2)...................(n^2)")
n= int(input("Enter the value of n :"))
sum=0
for i in range(1,n+1):
     sum+=i**2
print("Sum of series :",sum)
