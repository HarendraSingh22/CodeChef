    t=input()
    for i in range(t):
        ip=raw_input().split()
        cost1,cost2=0,0
        for j in range(int(ip[0])):
                l=raw_input()
                for y in range(int(ip[1])):
                    if(j%2==0):
                        if(y%2==0):
                           if(l[y]!="G"):
                                cost1=cost1+5
                        else:
                            if(l[y]!="R"):
                                cost1=cost1+3
                    else:
                        if(y%2!=0):
                           if(l[y]!="G"):
                                cost1=cost1+5
                        else:
                            if(l[y]!="R"):
                                cost1=cost1+3
                        
                        
                for y in range(int(ip[1])):
                    if(j%2!=0):
                        if(y%2==0):
                           if(l[y]!="G"):
                                cost2=cost2+5
                        else:
                            if(l[y]!="R"):
                                cost2=cost2+3
                    else:
                        if(y%2!=0):
                           if(l[y]!="G"):
                                cost2=cost2+5
                        else:
                            if(l[y]!="R"):
                                cost2=cost2+3
                        
                        
        if(cost1>cost2):
            print(cost2)
        else:
            print(cost1)
            
                 
