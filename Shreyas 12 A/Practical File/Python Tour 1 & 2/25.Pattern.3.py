# Pattern.3
a=1
for i in range(3,0,-1):
    for j in range(i-1):
        print("  ",end="")
    for k in range(0,a):
        print("*",end="")
    a+=2
    for l in range(i-1):
        print("   ",end="")
    print()
