fileout=open("STRS.txt",'w')
string=""
ans='y'
while ans.lower()=='y':
    line=input("Enter what is to be written on the file")
    string+=(line + '\n')
    ans=input("Enter 'y' to add more lines and 'n' to exit :" )
fileout.write(string)
fileout.close()
print("Record Added!! ")
    
    