import sys

a,b=map(int,sys.stdin.readline().split())
ans_list=[]
for i in range(1,a+1):
    if a%i==0:
        ans_list.append(i)
print(len(ans_list))
if len(ans_list)<b:
    print(0)
else:
    print(ans_list[b-1])