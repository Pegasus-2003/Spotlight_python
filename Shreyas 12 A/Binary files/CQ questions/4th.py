def Display_words():
    file=open("letr.txt",'r')
    line=file.read()
    word=line.split()
    for i in word:
        if len(i)<4:
            print(i)
    file.close()
    
Display_words()
