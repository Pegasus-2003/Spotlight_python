#Get a new string from the first 2 and the last 2 words the entered string
a=input("Enter the string :")
b=""
l=len(a)
b=a[0] +a[1] +a[l-2] +a[l-1]
print("Old string :",a)

print("Converted  string :",b)    
