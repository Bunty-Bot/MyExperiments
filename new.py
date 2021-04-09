a = int(input())

def repeat():
    b = int(input())
    c = int(input())
    if a=='1':
        print(b + c)
    elif a=='2':
        print(b - c)
    elif a=='3':
        print(b*c)
    elif a=='4':
        print(b/c)
    elif a=='5':
        print(b%c)
    elif a=='6':
        exit()
    else:
        print("Invalid Operation")

while a<=6:
    repeat()
    break