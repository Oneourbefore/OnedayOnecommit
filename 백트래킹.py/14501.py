n=int(input())
list1= [list(map(int,input().split())) for _ in range(n)]
dp=[0 for _ in range(n+1)]
print(list1)
# 7
# 3 10
# 4 50
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
# dp = [0, 0, 45, 35, 15, 0, 0]
for k in range(n-1,-1,-1):
    if k+list1[k][0]>n:
        dp[k]=dp[k+1]
        
    else:
        dp[k]=max(dp[k+1],list1[k][1]+dp[k+list1[k][0]])

print(max(dp))
print(dp)