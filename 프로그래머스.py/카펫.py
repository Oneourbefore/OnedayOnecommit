def solution(brown, yellow):
    posslist=[]
    num=brown+yellow
    for i in range(1,num+1):
        if num % i ==0:
            j=num//i
            if i>j and i>=3 and j>=3 and (i-2)*(j-2)==yellow:
                posslist.append([i,j])

    return posslist
print(solution(8,1))
# brown = 10 , yellow = 2 
# 두개를 더했을 떄 12 , [12,1] [6,2] [4,3]
# 두개를 더했을 떄 24 , [12,1] [6,2] [4,3]
