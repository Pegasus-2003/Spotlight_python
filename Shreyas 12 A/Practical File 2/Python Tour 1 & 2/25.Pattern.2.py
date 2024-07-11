# Pattern.2
string="ABCD"
y=0
for i in range(4,0,-1):
    y+=1 
    for n in range(i-1):
        print("   ",end="")
    for l in range(0,y):
        print(string[l],end="")
    print()
