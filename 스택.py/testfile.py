from collections import deque
a = deque([3, 2, 1, -1, 1])
print(a)
a.popleft()
a.rotate(-2)
print(a)
a.popleft()
a.rotate(-1) # 왼쪽으로 이동
print(a)

# 만약에 입력된 수가 양수일 때 왼쪽으로 이동하는거잖아 