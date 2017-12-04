    t=int(input())
    for i in range(t):
        n=int(input())
        op=0
        for x in range(2,n+n+1,1):
            k=(min(abs(1-x),abs(n+n+1-x)))
     
            d=0
            a=x
            while (a > 0):
                if (a % 2 == 0):
                    d = d + (a % 10)
                else:
                    d = d - (a % 10)
                a = int(a / 10)
     
            for y in range(k):
                op=op+abs(d)
     
        print(op)
