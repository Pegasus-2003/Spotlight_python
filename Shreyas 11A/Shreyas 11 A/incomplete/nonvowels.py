def nonvowels(text):
         nonvowels=0
         a=text.split()
         print(a)
         vowels=['a','i','e','o','u']
         for i in a:
                  for j in i:
                           if j not in vowels:
                                    nonvowels+=1
         return nonvowels
x=input('enter the strings')
print(nonvowels(x))
