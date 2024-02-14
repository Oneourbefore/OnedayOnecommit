a=int(input())
list_right=list(map(int,input().split()))
# 만약 4 5 1 3 2
# 1 2 3 4 5 
# 2 1 3 4 5
# 오른쪽에 있는 부분은 오름차순이여야 하고 아래 있는 부분은 도 오름차순이여야함
# i=1
# list_down=[]
# for _ in range(a):
#     popnum=list_right.pop(0)
#     if popnum==i:
#         i=i+1
#     else:
#         list_down.append(popnum)
# for k in range(len(list_down)-1):
#     if list_down[k]-1!=list_down[k+1]:
#         printstr="Sad"
#         break
#     else:
#         printstr="Nice"+
# print(printstr)
list_down=[]
k=1
# 5 4 1 3 2 
for _ in range(a):
    popnumber=list_right.pop(0)
    if popnumber==k:
        k=k+1
        print(k)
    else:
        list_down.append(popnumber)
        
    for _ in range(len(list_down)):
        print(list_down)
        print(k)
        if list_down[-1]==k:
            k=k+1
            list_down.pop()

if len(list_right)==0 and len(list_down) ==0:
    print("Nice")
else:
    print("Sad")