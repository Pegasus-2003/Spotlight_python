# Checking presence of value in dicitonary
info={'riya':'cs','mark':'eco','sihpreet':'eng','kamal':'env'}
a=input("Enter the value to be searched for :")
if a in info.values():
    for i in info:
        if info[i]==a:
            print("The key of the given value is",i)
            break
    else:
        print("Given value does not exist")
