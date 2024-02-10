while True:
    k=int(input())
    sum=0
    ans_list=[]
    if k==-1:
        break
    else:
        for i in range(1,k):
            if k%i==0:
                sum=sum+i
                ans_list.append(str(i))
        if k==sum:
            result=" + ".join(ans_list)
            print(str(k)+" = "+result)
        else:
            print(str(k)+' is NOT perfect.')
    