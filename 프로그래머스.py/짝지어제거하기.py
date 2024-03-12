def solution(s):
    answer=0
    list1=[]
    for i in range(len(s)):
        if len(list1)==0:
            list1.append(s[i])
        elif list1[-1]==s[i]:
            list1.pop()
        else:
            list1.append(s[i])
    if len(list1) == 0:
        return 1
    return answer

# 내가 생각한 전략 ?
# 만약에 같은 쌍이 존재하는 곳에 도달했으면 그 쌍을 제거하고 처음부터 다시 시작하는거

