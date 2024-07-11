# Length of the longest word of the list
lst=eval(input("Enter a list of words :"))
length=0
for i in lst:
    if len(i)>length:
        length=len(i)
print("The length of the  longest word in the list is :",length)
