#Program that repeatedly inputs numbers until done is typed
sum=0
while True:
    ch=input("Enter the character :")
    if ch=="Done " or ch=="done":
        break
    else:
        b=float(ch)
        sum+=b
print("Sum :",int(sum))
