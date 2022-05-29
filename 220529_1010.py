N,m,M,T,R = map(int, input("").split())

a=0
defaultGap=m
time=0
weight=0
while weight<N:
    if defaultGap+T > M:
        print("-1")
        a=1
        break
    if m+T <= M:
        m+=T
        time+=1
        weight+=1

    else: #쉬는시간
        if m-R<defaultGap:
            m=defaultGap 
            time+=1
        else:   
            m-=R
            time+=1

if a!=1:
    print(time)