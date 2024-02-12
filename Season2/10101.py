list1=[]
for _ in range(3):
    a=int(input())
    list1.append(a)

if sum(list1)!=180:
    print('Error')

elif sum(list1)==180 and (list1[0]!=list1[1] and list1[1]!=list1[2] and list1[0]!=list1[2]):
    print("Scalene")

elif list1[0]==60 and list1[1]==60 and list1[2]==60:
    print("Equilateral")

else:
    print('Isosceles')