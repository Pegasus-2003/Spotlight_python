# Series.3 =  1 + (1+2) + (1+2+3)+........(1 +2 + 3 +....n)
n= int(input("Enter the value of n :"))
a=0
for i in range(1,n+1):
     for j in range(i+1):
          a+=j
print("Sum of series :",a)
