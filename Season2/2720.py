testcase=int(input())

for _ in range(testcase):
    q=0
    d=0
    n=0
    p=0
    money=int(input())

    if money >= 25:
        q=money//25
        money=money%25
    if money >= 10:
        d=money//10
        money=money%10

    if money >= 5:
        n=money//5
        money=money%5
    if money >= 1:
        p=money
    print(q,d,n,p)
    