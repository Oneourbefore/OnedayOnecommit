a=input()
list1=[0]*10
for i in a:
    i=int(i)
    if i==6 or i==9:
        list1[5]=list1[5]+1
    else:
        list1[i-1]=list1[i-1]+1

list1[5]=(list1[5]+1)//2
print(max(list1))
# 9999 -> 2 // 122 -> 2 9가 들어왔을 때 9가 하나 더 들어왔거나 6이 들어오면 하나씩 추가 6이 들어와도 마찬가지의 규칙을 가짐 .  