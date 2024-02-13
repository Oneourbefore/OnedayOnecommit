# 28278
# list1=[2,3,4,5]
# print(list1.pop())
# print(list1)
import sys
a=int(sys.stdin.readline())
stack_list=[]
for _ in range(a):
    inputnum=sys.stdin.readline().split()

    if int(inputnum[0])==4:
        if len(stack_list)==0:
            print(1)
        else:
            print(0)

    elif int(inputnum[0])==1:
            stack_list.append(int(inputnum[1]))

    elif int(inputnum[0])==2:
            if len(stack_list)!=0:
                print(stack_list.pop())
            else:
                print(-1)

    elif int(inputnum[0])==3:
            print(len(stack_list))



    elif int(inputnum[0])==5:
            if len(stack_list)!=0:
                print(stack_list[-1])
            else:
                print(-1)