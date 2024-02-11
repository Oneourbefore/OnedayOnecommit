import sys
a=int(input())
listx=[]
listy=[]
for _ in range(a):
    x,y=map(int,sys.stdin.readline().split())
    listx.append(x)
    listy.append(y)

print((max(listx)-min(listx))*(max(listy)-min(listy)))

