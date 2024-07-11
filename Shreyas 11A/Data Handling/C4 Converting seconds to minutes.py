#program to accept seconds and print in minutes
time= int(input("Enter the time in second = "))
min =  time // 60
second = time%60
print("Time = ",min,"Mins",second,"Second ")
