# 12345 21345 21435 31425 
a,b=map(int,input().split())
list1=[i for i in range(1,a+1)]
for k in range(b):
    x,y=map(int,input().split())
    list1[x-1],list1[y-1] = list1[y-1] , list1[x-1]

print(*list1)