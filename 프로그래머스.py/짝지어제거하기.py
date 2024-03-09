def solution(s):
    answer = -1
    s=list(s)
    k=s[0]
    # s = baabaa
    for chars in range(1,len(s)):
        print(k,s[chars])
        if k==s[chars]:
            s=s.pop(chars)
        else:
            k=s[chars]
    return answer
# 내가 생각한 전략 ?
# 만약에 같은 쌍이 존재하는 곳에 도달했으면 그 쌍을 제거하고 처음부터 다시 시작하는거

print(solution('baabaa'))    