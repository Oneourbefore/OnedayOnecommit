a,b=map(int,input().split())
list_map=[]
for _ in range(b):
    list_map.append(list(map(int,input().split())))

def makewall(count):
    if count ==3:
        print(list_map)
        return
    for i in range(a):
        for j in range(b):
            if list_map[i][j]==0:
                list_map[i][j]=1
                makewall(count+1)
                list_map[i][j]=0
makewall(0)