makesum=0
makesum1=0
for _ in range(20):
    a,b,c=input().split()
    if c=='A+':
        makesum=makesum+4.5*float(b)
        makesum1=makesum1+float(b)
    elif c=='A0':
        makesum=makesum+4*float(b)
        makesum1=makesum1+float(b)

    elif c=='B+':
        makesum=makesum+3.5*float(b)
        makesum1=makesum1+float(b)

    elif c=='B0':
        makesum=makesum+3*float(b)
        makesum1=makesum1+float(b)

    elif c=='C+':
        makesum=makesum+2.5*float(b)
        makesum1=makesum1+float(b)


    elif c=='C0':
        makesum=makesum+2*float(b)
        makesum1=makesum1+float(b)

    elif c=='D+':
        makesum=makesum+1.5*float(b)
        makesum1=makesum1+float(b)

    elif c=='D0':
        makesum=makesum+float(b)
        makesum1=makesum1+float(b)

    elif c=='F':
        makesum=makesum
        makesum1=makesum1+float(b)
    elif c=='F':
        makesum=makesum
        makesum1=makesum1



print(makesum/makesum1)