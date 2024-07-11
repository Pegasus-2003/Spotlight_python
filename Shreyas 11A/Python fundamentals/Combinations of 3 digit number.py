#Different combinations of a 3 digit number
A=int(input("Entre a 3 digit number :"))
B=A%10
C=A/10
D=int(C)
E=D%10
F=D/10
G=int(F)
print("The different combinations of",A,"are: ")
print("1)",B*100+E*10+G)
print("2)",B*100+G*10+E)
print("3)",G*100+E*10+B)
print("4)",G*100+B*10+E)
print("5)",E*100+B*10+G)
print("6)",E*100+G*10+B)
                                                          
