#from fractions import gcd
def find_gcd(x, y):
     
    while(y):
        x, y = y, x % y
     
    return x

arrlength,q=list(map(int,input().strip().split()))
arr=list(map(int,input().strip().split()))
w=arrlength
h=arrlength+1
arrgcd=[[0 for x in range(w)] for y in range(h)] 
arrgcd[0]=arr

for i in range(arrlength):
    for j in range(4,arrlength-i+3):
        arrgcd[i+1].append(find_gcd(arrgcd[i][j+4],arrgcd[0][i+j]))
        
        
print(arrgcd)
