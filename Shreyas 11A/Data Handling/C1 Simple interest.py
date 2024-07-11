#Program for simple interest
principal = int(input("Enter principal amount = "))
rate = int(input("Enter rate = "))
time = int(input("Enter time = "))
si = principal * rate * time / 100
print("Simple Interest = ",si)
