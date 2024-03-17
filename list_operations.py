lst=[]
n=int(input("no of operations to be performed on the list:\n"))
for i in range(n):
    s=input().split()
    if s[0]=="insert":
        lst.insert(int(s[1]),int(s[2]))
    elif s[0]=="sort":
        lst.sort()
    elif s[0]=="append":
        lst.append(int(s[1]))
    elif s[0]=="remove":
        lst.remove(int(s[1]))
    elif s[0]=="print":
        print(lst)
    elif s[0]=="pop":
        lst.pop()
    elif s[0]=="reverse":
        lst.reverse()
    else:
        print("please enter valid operation")
        exit(0);
