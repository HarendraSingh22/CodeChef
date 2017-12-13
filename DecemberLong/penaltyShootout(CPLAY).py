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
                        print("TEAM-A "+str(i+1))
                        break
                    if(b>(a+((9-i)/2))):
                        print("TEAM-B "+str(i+1))
                        break
                else:
                    if(int(ip[i])==1):
                        b=b+1
                    if(b>(a+((10-i)/2))):
                        print("TEAM-B "+str(i+1))
                        break
                    if(a>(b+((9-i)/2))):
                        print("TEAM-A "+str(i+1))
                        break
                
            else:
                if(i==19 and int(ip[19])==0):
                    print("TIE")
                    break
                
                if(i%2==0 and int(ip[i])==1 and int(ip[i+1])==0):
                    print("TEAM-A "+str(i+2))
                    break
                if(i%2!=0 and int(ip[i])==1 and int(ip[i+1])==0):
                    print("TEAM-B "+str(i+2))
                    break
    except EOFError:
        break
