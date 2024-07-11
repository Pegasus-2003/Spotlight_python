# creating binary file and storing records
s=20
with open("NAMES.dat",'wb') as f:
    ans='y'
    while ans.lower()=='y':
        name=input("Enter name ")
        l=len(name)
        name=name+(s-l)*' '
        name=name.encode()
        f.write(name)
        ans=input("y/n? ")

