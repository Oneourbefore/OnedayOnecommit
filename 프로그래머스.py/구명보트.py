# def solution(people, limit):
#     answer = 0
#     return answer
# from itertools import combinations, permutations
# nums = [70,50,20,10]
# numslist=[ i for i in range(1,len(nums)+1)]
# combi = list(combinations(numslist, 2))
# for a,b in combi:
#     a=a-1
#     b=b-1
#     ans=[]
#     realans=[]
#     for k in range(len(nums)):
#         print(a,b)
#         if k == a or k == b:
#             ans.append(nums[k])
#         else:
#             realans.append(nums[k])
#     realans.append(sum(ans))
#     print(realans)
# peoplelist=[70,50,20,10]
# peoplelist.sort()
# def solution(people, limit):
#     answer=0
#     people.sort() # 정렬하기 
#     a=0
#     b=len(people)-1
#     while a<b:
#         if people[a]+people[b]<=limit:
#             a=a+1
#             answer+=1
#         else:
#             answer+=1
# print(peoplelist)
def solution(people, limit) :
    answer = 0
    people.sort()
    a = 0
    b = len(people) - 1
    while a < b : # a=0 , b=3 
        if people[b] + people[a] <= limit : # 만족 a = 1 answer = 1  b= 2 , a = 2 answer =2 b = 1
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
print(solution([70, 50, 80, 50],100))
# 50 50 70 80 => 