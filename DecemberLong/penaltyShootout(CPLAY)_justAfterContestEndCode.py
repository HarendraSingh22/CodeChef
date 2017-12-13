while(1):
    try:
        ip=input()
        if(len(ip)==0):
            break
        a,b=0,0
        for i in range(20):
            if(i<10):
                if(i%2==0):
                    if(int(ip[i])==1):
                        a=a+1
                    if(a>(b+((10-i)/2))):
                        print("\nTEAM-A "+str(i+1),end="")
                        break
                    if(b>(a+((9-i)/2))):
                        print("\nTEAM-B "+str(i+1), end='')
                        break
                else:
                    if(int(ip[i])==1):
                        b=b+1
                    if(b>(a+((10-i)/2))):
                        print("\nTEAM-B "+str(i+1), end='')
                        break
                    if(a>(b+((9-i)/2))):
                        print("\nTEAM-A "+str(i+1), end='')
                        break
                
            else:
                if(i==19 and int(ip[19])==0):
                    print("\nTIE",end='')
                    break
                
                if(i%2==0 and int(ip[i])==1 and int(ip[i+1])==0):
                    print("\nTEAM-A "+str(i+2), end='')
                    break
                if(i%2!=0 and int(ip[i])==1 and int(ip[i+1])==0):
                    print("\nTEAM-B "+str(i+2), end='')
                    break
    except EOFError:
        break
