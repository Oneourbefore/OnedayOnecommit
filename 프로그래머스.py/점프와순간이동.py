# def solution(n):
#     dp=[k for k in range(1,n+1)]
#     # 만약 n이 5면 [1,2,3,4,5]
#     num=1
#     for k in range(2,n+1):
#         while k*num<n:
#             dp[k]
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')
#     # 5000 -> 5 
#     # 2 4 8 16 32 
#     # 3 6 12 24 
#     # 4 
#     return ans

# # 10 [0,1,2,0,0,0,0,0,0,0,0]

def solution(n):
    answer=1
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n-1
            answer=answer+1
    return answer
print(solution(5000))
# 5 -> 4 +1 -> 2  - > 1