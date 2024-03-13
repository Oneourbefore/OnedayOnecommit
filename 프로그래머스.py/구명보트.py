# def solution(people, limit):
#     answer = 0
#     return answer
from itertools import combinations, permutations

nums = [70,50,20,10]
numslist=[ i for i in range(1,len(nums)+1)]
combi = list(combinations(numslist, 2))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
for a,b in combi:
    ans=[]
    realans=[]
    for k in range(len(nums)):
        print(a,b)
        if k == a or k == b:
            ans.append(nums[k])
        else:
            realans.append(nums[k])
    realans.append(sum(ans))
    print(realans)