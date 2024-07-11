#capitalizing first letter of the word:
line=input("Enter a line :")
l=len(line)
string=" "
for i in range(0,l,2):
    string+=line[i]
    if i<(l-1):
        string+=line[i+1].upper()
print("Capitalized :",string)
        
        
    
