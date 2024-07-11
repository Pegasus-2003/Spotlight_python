#occurences of substring in line
line=input("Enter a line :")
sub=input("Enter substring :")
l= len(line)
m=len(sub)
start=0
end=l+1
count=0
while True:
    pos=line.find(sub,start,end)
    if pos!=-1:
        count+=1
        start=pos+m
    else:
        break
    if start>=l:
        break
print("The sub string :",sub,",occurs",count,"times in the line")
    
