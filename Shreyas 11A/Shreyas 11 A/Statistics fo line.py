#Printing Statistics of a line
ine=input("Enter a line :")
lower_count=upper_count=0
digit_count=alpha_count=0
for a in line:
    if a.islower():
        lower_count+=1
    elif a.isupper():
        upper_count+=1
    elif a.isdigit():
        digit_count+=1
    if a.isalpha():
        alpha_count+=1
print( "Lowercase count =",lower_count )
print("Uppercase count =",upper_count)
print("Digit counts =",digit_count)
print("Alphabets count =",alpha_count)
  
        
