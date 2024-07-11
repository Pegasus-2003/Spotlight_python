#Armstrong number
n=int(input("Enter a number :"))
string=str(n)
sum=0
num=n
l=len(string)
for i in range(0,l):
    digit=n%10
    n=int(n/10)
    sum+=digit**3
if sum==num:
    print("It is an armstrong number !")
else:
    print("It is  not an armstrong number !")
