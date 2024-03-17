# # N A B answre , 8 4 7 3 
# # 4번 3번 1, 2 4번과 7번 
# # 1 , 2 , 4  , 8 

# # list1=[ i for i in range(1,9)]
# # [[1,2],[3,4],[5,6][7,8]] ->1
# # [[2,4],[6,7]] ->2
# # [4,6] ->3
# # n = 8 5 7 ->  
# # 8기준 4이상 4이하 검사함 
# # 4이상 기준 6이상 6이하 검사함 // 4이하 기준 2이상 2이하 검사함
# # 만약 N = 8 일때 두 숫자가 4 이상이면 => 6 이상과 이하
# # 만약 N = 8 일때 하나는 4  이상 , 하나는 4 이하면 => 끝
# # n = 8 ,, a=4 , b=3 => 4로 되고 4,3 이 나옴  
# # n = 8 ,, a=1 , b=2 => 4,1,2 
# # n = 8 ,, a=1 , b=4 => 4,1,4 의 경우에 
# def solution(n,a,b):
#     answer = 0
#     if ((a<=n//2 and b>n//2) or (a>n//2 and b<=n//2)) or ((a<=n//2 and b>n//2) or (a>n//2 and b<=n//2)):
#             while True:
#                 n=n//2
#                 answer=answer+1
#                 if n==1:
#                     break
#             return answer
#     else:
#         if n==1:
#             answer=1
#             return answer
#         else:
#             return(solution(n//2,a,b))
# # 1 - 8 
# # 16 -> 4, 8 ,12 (5,7)  
# # 12 -> 5 8
# print(solution(16,5,8))
def solution(n, a, b):
    answer = 0
    
    while a != b:  # A와 B가 만날 때까지 반복
        answer += 1  # 라운드 수 증가
        # A와 B의 번호를 다음 라운드로 갱신
        a = (a + 1) // 2
        b = (b + 1) // 2
    
    return answer

# 예시 입력에 대한 출력
print(solution(8, 4, 7))