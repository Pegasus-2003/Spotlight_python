#program to find stats of sentence
line=input("Enter a sentence")
length=len(line)
print("No of characters are :",length)
words=1
alnum=0
for a in line:
    if a==" ":
        words+=1
    if a.isalnum():
        alnum+=1
print("No of words :",words)
print("Percentage of alphanumeric charcters is :",(alnum/length)*100)
