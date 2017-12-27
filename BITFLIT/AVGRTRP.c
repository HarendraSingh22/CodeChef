//something is wrong in this one which I am not noticing now !

//this is the simple basic correct program. something maybe I am getting wrong !
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n;
    scanf("%d",&n);
    for(int x=0;x<n;x++)
    {
        long long int rope=0;
        int y;
        scanf("%d",&y);
        long int arr[2][y];
        for(int i=0;i<2;i++)
        {   
            for(int j=0;j<y;j++)
            {
                scanf("%li",&arr[i][j]);
            }
        }
        for(int i=0;i<2;i++)
        {   
            for(int j=0;j<y;j++)
            {
                printf("%li  ",arr[i][j]);
            }
            printf("\n");
        }
        
        
       for(int i=0;i<y-1;i++)
       {
           for(int j=i+1;j<y;j++)
           {
               
               
            if(arr[1][i]>=arr[1][j])
            {
                
                rope=rope+(arr[1][i]*(abs(arr[0][i]-arr[0][j])));
               
            }
            else
            {
                rope=rope+(arr[1][j]*(abs(arr[0][i]-arr[0][j])));
            }
           }
       }
       printf("%lli \n",rope);
    }
    return 0;
}
