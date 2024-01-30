#가로 세로의 크기가 
import sys
input= sys.stdin.readline
paper=[[0]*101 for i in range(101)]
for _ in range(int(input())):
   a,b=map(int,input().split())
   for i in range(10):
      for j in range(10):
        
        paper[a+i][b+j]=1
a=0
for j in paper:
   a=a+sum(j)

print(a)
   
