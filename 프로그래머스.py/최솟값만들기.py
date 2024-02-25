def solution(A,B):
    A=sorted(A,reverse=True)
    B=sorted(B)
    answer=0
    for i in range(len(A)):
        answer=answer+A[i]*B[i]
    return answer

print(solution([1, 4, 2],[5, 4, 4]))