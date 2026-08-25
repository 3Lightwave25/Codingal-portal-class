n=5
for i in range(1,n+1):
    num=1
    for j in range(n-i,0,-1):
        print(" ",end="")
    for k in range(2*i-1):
        print(num,end="")
        num+=1
    print()
for i in range(1,n+1):
    num=1
    for j in range(i):
        print(" ",end="")
    for k in range(2*(n-i)-1):
        print(num,end="")
        num+=1
    print()


