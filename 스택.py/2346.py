# from collections import deque
# import sys
# d=deque()
# 3 -> -3 -> -1 -> 1 -> 2 
# -1 3 2 1 /3 2 1 -1
# deque에서 사용되는 rotate 메서드를 사용하기?
# 만약에 숫자 3이 처음이면 오른쪽으로 3칸 이동하잖아 3이 있는 상태에서, 그리고 3을 지운단말이야 -3 -1 2 1   -1 2 1 / 1 -1 2
from collections import deque
import sys

anslist=[]
real_ans_list=[]
a=int(sys.stdin.readline())

movelist = deque([i for i in range(1,a+1)]) # 1 , 2 , 3 , 4 , 5 
usedeque = deque(list(map(int,sys.stdin.readline().split())))

firstnum = usedeque.popleft()
movenum = movelist.popleft()
real_ans_list.append(movenum)

for _ in range(a-1):
    # usedeque = [3,2,1,-3,-1] -> rotate(1) -> [-1,3,2,1,-3]
    if firstnum>0:
        usedeque.rotate(-(firstnum-1))
        movelist.rotate(-(firstnum-1))
        firstnum=usedeque.popleft()
        movenum=movelist.popleft()
        real_ans_list.append(movenum)
    else:
        usedeque.rotate(-firstnum)
        movelist.rotate(-firstnum)

        firstnum=usedeque.popleft()
        movenum=movelist.popleft()
        real_ans_list.append(movenum)
print(*real_ans_list)