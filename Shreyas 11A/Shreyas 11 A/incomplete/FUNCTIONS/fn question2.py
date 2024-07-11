def increment(n):
    n.append([49])
    return(n[0],n[1],n[2],n[3])
l=[23,35,47]
m1,m2,m3,m4=increment(l)
print(l)
print(m1,m2,m3,m4)
print(l[3]==l[4])
