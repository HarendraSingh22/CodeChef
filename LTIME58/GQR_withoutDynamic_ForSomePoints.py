from fractions import gcd
 
 
arrlength,q=input().strip().split()
arrlength=int(arrlength)
q=int(q)
arr=list(map(int,input().strip().split()))
 
for j in range(q):
    x,y=list(map(int,input().strip().split()))
    l = arr[x-1:y]
    maxgcd=gcd(l[0],l[1])
 
    for i in range(len(l)):
        for j in range(len(l)):
            if(j==i):
                continue
            maxgcd=max(gcd(l[i],l[j]),maxgcd)
   
    print(maxgcd)
