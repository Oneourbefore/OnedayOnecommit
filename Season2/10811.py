# 1 2 3 4 5 
# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5
a,b=map(int,input().split())
list1=[ i+1 for i in range(a)]
for k in range(b):
    x,y=map(int,input().split())
    list1[x-1:y]=reversed(list1[x-1:y])
print(*list1)