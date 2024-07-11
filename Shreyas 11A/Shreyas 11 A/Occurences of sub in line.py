#No of occcureneces of substring in a line
line=input("Enter a line :")
sub=input("Enter substring :")
length=len(line)
lensub=len(sub)
start=count=0
l=length
while True:
    pos=line.find(sub,start,l)
    if pos!=-1:
        count+=1
        start=pos+lensub
    else:
        break
    if start>=length:
        break
print("No of occureneces of", sub,"is :",count)
