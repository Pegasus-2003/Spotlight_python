# No of words that have less than 4 characters
def DISPLAY_WORDS(n):
    f=open(n,'r')
    s=f.read()
    l=s.split()
    for i in l:
         if len(i)<4:
             print(i)

DISPLAY_WORDS(“story.TXT")
