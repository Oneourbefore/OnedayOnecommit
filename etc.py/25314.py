a=int(input())
if a==4:
    print('long int')
else:
    b=a//4
    k=''
    for i in range(b-1):
        k=k+'long '
    
    print(k+'long int')