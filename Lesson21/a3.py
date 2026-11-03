tuplex = (0,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0) 
s = 0
r = 0
for i in range(0,17):
    if tuplex[i]==0:
        s=s+1
    else:
        r=r+1

if s>r:
    print("The weather today is good.")
else:
    print("The weather today is bad.")


