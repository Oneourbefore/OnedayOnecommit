def solution(n):
    dp=[0]*100002
    dp[0]=0
    dp[1]=1
    for i in range(n):
        dp[i+2]=dp[i]+dp[i+1]
    return dp[n]%1234567
print(solution(100000))