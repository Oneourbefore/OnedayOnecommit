# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 
# 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다. 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.

# 5 4
# 1 2 3
# 3 4 4
# 1 4 1
# 2 2 2
# ans : 1 2 1 1 0

a,b = map(int,input().split())
list1= [ 0 for k in range(a)]
for i in range(b):
    x,y,z=map(int,input().split())
    for k in range(x-1,y):
        list1[k]=z

print(*list1)