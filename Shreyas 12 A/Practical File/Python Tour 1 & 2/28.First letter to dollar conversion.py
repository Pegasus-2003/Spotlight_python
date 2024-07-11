# First letter of word replaced by dollar symbol
line=input("Enter a line :")
l=len(line)
i=0
string=" "
while i < l:
    if i==0:
        string+="$"
        i+=1
    elif (line[i]==" " and line[i+1]!=" "):
        string+=line[i]
        string+= "$"
        i+=2
    else:
        string+=line[i]
        i+=1
print("Entered string :",line)
print("Converted string :",string)
        
    
