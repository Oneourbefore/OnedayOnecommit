# a b c d e f 
# x+3y=-1
# 4x+ 1y = 7
import sys

a,b,c,d,e,f=map(int,sys.stdin.readline().split())
for i in range(-999,999):
    for j in range(-999,999):
        if a*i+b*j==c and d*i+e*j==f:
            print(i,j)
            break