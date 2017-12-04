    #include<stdio.h>
    #include<stdlib.h>
     
    void main()
    {
        long long int t,n,i,k,a,op=0,d=0,x,y;
        scanf("%lli",&t);
        while(t>0)
        {
            scanf("%lli",&n);
            op=0;
            for(i=2;i<=n+n;i++)
            {
                x=abs(1-i);
                y=abs(n+n+1-i);
                if(x>=y)
                    k=y;
                else
                    k=x;
               
                d=0;
                a=i;
                while(a>0)
                {
                    if(a%2==0)
                        d=d+a%10;
                    else
                        d=d-a%10;
                    a=a/10;
                }
                
                    op=op+(k*abs(d));
            }
            printf("%lli\n",op);
            t--;
        }
    }
     
