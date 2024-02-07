a=input()
num=len(a)//2   
if len(a)%2!=0:  
    if a[:num]==a[num+1:][::-1]:
        print(1)
    else:
        print(0)
else:
    if a[:num]==a[num:][::-1]:
        print(1)
    else:
        print(0)