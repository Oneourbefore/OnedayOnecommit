list1=[[0 for i in range(15)] for i in range(5)]
for i in range(5):
    a=input()
    for k in range(len(a)):
        list1[i][k]=a[k]
output=''
for k in range(15):
    for i in range(5):
        if type(list1[i][k]) == int:
            continue
        else:
            output=output+str(list1[i][k])

print(output)