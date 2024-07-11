#Numbers that are perfect square and sum of the digits less than 10
a=int(input("Enter the start of range :"))
b=int(input("Enter the end of range :"))
lst=[]
lst1=[]
for i in range(a,b+1):
    if (i**0.5)% 1==0 :
        lst.append(i)
for j in lst:
    sum=0
    ele=j
    while j>0:
        digit=j%10
        j=int(j/10)
        sum+=digit
    if sum<=10:
        lst1.append(ele)
print( "List of number in range that are perfect squares and sum of digits less than 10 : ")
print(lst1)
        
        
