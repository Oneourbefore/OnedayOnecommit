import sys

a=int(sys.stdin.readline())
enter_list={}

for _ in range(a):
    name,state=map(str,sys.stdin.readline().split())
    if state == 'enter':
        if name not in enter_list:
            enter_list[name]=state
    elif state == 'leave':
        if name in enter_list:
            del enter_list[name]

sorted_names = sorted(enter_list.keys(), reverse=True)
#딕셔너리를 정렬할 때는 key를 가져와서 reverse 사용하기
for name in sorted_names:
    print(name)

# 왜 시간초과가 날까
    