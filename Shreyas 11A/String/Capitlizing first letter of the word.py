#capitalizing first letter of the word:
line=input("Enter a line :")
l=len(line)
i=0
string=" "
while i < l:
    if i==0:
        string+=line[0].upper()
        i+=1
    elif (line[i]==" " and line[i+1]!=" "):
        string+=line[i]
        string+= line[i+1].upper()
        i+=2
    else:
        string+=line[i]
        i+=1
print("Capitalized sentence :",string)
        
    
