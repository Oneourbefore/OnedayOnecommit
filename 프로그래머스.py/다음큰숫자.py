# 1111 8 + 4 + 2 + 1 = 15
# 10111 16 + 4 + 2 + 1 = 23
# 11011 16 + 8 + 2 + 1 = 27
# 11101 16 + 8 + 4 + 1 = 29
# 11110 16 + 8 + 4 + 2 = 30
# 100111 32 + 
# 조합을 사용하여 
def check(x):
    binary = bin(x) # 이진수로 변환하기
    one = binary.count('1') # 개수를 셈
    return one  # 개수를 저장함 One이라는 변수에 저장해놓기 

def solution(n):
    # 78 
    # num = 3
    answer = n
    num = check(n)
    while True:
        answer += 1 # 값을 높이면서 1의 갯수가 같은지 확인하기 
        if int(check(answer)) == num:
            return answer