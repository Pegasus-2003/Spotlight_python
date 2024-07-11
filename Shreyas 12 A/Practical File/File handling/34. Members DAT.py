
import pickle

member1={}


def member():
    file=open("members.dat",'a+b')
    n=int(input("Input number of entries :"))
    for i in range(n):
        no=int(input("Input member number :"))
        name=input("Input member name :")
        member1[no]=name
        pickle.dump(member1,file)
    file.close()
    
def update():
    with open('members.dat', 'ab') as f:
        dicti = {}
        n = input('Enter member number : ')
        name = input("Enter member name : ")
        dicti[n] = name
        member1.update(dicti)
        pickle.dump(eval(str(member1)), f)


def read_file():
    data = ' '
    with open('members.dat', 'rb') as file:
        try:
            while data:
                data = eval(str(pickle.load(file)))
                for i, j in data.items():
                    print(i, j)
        except EOFError:
            file.close()


while True:
    print('1 . TO ADD DATA    2 . TO UPDATE     3. TO READ')
    ch = input('Enter your choice : ')
    if ch == '1':
        member()
        break
    elif ch == '2':
        update()
        break
    elif ch=='3':
        read_file()
        
    else:
        print("Wrong Input Retry")
        continue
