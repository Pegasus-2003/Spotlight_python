import pickle

def write():
    ans = 'y'
    m = []
    while ans.lower() == 'y':
        f = open("company.dat", 'wb+')
        cid = input("Enter the comp ID ")	
        cna = input("Enter C NAME ")
        tu=input("Turnover")
        company = {}
        company["COMPANY ID"] = cid
        company["C NAME"] = cna
        company["TURNOVER"]=tu
        m.append(company)
	ans = input("Continue ?")
pickle.dump(m, f)
    f.close()
f = open("company.dat", ‘rb+')
emp = []
    while True:
        try:
            emp = pickle.load(f)
        except EOFError:
            break
    print("%15s" % "C ID ", "%20s" % "C NAME ", "%20s" % "TURNOVER")
    for i in emp:
        j = list(i.values())

        print()
        if j[0] == "1005":
            print("%15s" % j[0], "%20s" % j[1], "%20s" % j[2])

write()


    

    
    
