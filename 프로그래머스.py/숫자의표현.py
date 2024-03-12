# greedy
def solution(n):
    answer=0
    listans=[ i for i in range(1,n+1)]
    for j in range(1,n+1):
        for k in range(1+n-j):
            if sum(listans[k:k+j])==n:
                answer=answer+1
                break
    return answer
# 1, 2 ,3 ,4 ,5 ,6 ,,
print(solution(15))