#Such a shitty problem. Like meant for small kids ! I won't do as mentioned , this is not school kids ! Make better questions when you host on CodeChef,etc !

n=input()
w,h=n,n # or w=h=n
Matrix = [[0 for x in range(w)] for y in range(h)] 
for i in range(n):
    l=raw_input().strip().split()
    for j in range(n):
        Matrix[i][j]=l[j]

for i in range(n):
    for j in range(n):
        print Matrix[n-j-1][i],
    print ("")
        
        
        #They dont allow python !
        #what kind of a contest doesnt allow python !!!!!!!!!!! This was insane !
