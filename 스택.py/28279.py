from collections import deque
import sys
d=deque()

# 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
# 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
# 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 5: 덱에 들어있는 정수의 개수를 출력한다.
# 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
# 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.

a=int(sys.stdin.readline())
for _ in range(a):
    inputnum=input().split()
    if int(inputnum[0])==6:
        if len(d)==0:
            print(1)
        else:
            print(0)
    elif int(inputnum[0])==1:
        d.appendleft(int(inputnum[1]))
    elif int(inputnum[0])==2:
        d.append(int(inputnum[1]))
    elif int(inputnum[0])==7:
        if len(d)!=0:
            print(d[0])
        else:
            print(-1)
    elif int(inputnum[0])==8:
        if len(d)!=0:
            print(d[-1])
        else:
            print(-1)
    elif int(inputnum[0])==5:
        print(len(d))
    elif int(inputnum[0])==3:
        if len(d)!=0:
            print(d.popleft())
        else:
            print(-1)
    elif int(inputnum[0])==4:
        if len(d)!=0:

            print(d.pop())
        else:
            print(-1)