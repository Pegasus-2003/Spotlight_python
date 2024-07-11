#To check is pallandrome or no
while True :
    a = input("Enter a number (To quit enter q ) : ")
    if a == "q" or a== "Q" :
        break
    else :
        reverse = a[  -1 : - len(a) - 1  : -  1]
       
        if a  ==  reverse :
            print(a,"is  a pallindrome")
        else :
            print(a,"is  not a pallindrome")
