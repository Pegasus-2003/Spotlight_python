#PROGRAM TO CHECK IF THE INPUT NUMBER IS 1, 2, 3 DIGIT OR OTHER THAN THIS
n=int(input("Enter the number "))
if n>999:
    print("Invalid input ")
else:
    if n>99:
        print("3 digit")
    elif n>9:
        print("2 digit")
    elif n>=0:
        print("1 digit")
    else:
        print("Invalid input ")
