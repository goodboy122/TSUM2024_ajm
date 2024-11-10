import sys
n,m=map(int, sys.stdin.readline().split())
pocket=[0 for i in range(n)]
min=max=num=0
for i in range(m):
  min,max,num=map(int, sys.stdin.readline().split())
  for j in range(min-1,max,1):
    pocket[j]=num;
  min=max=num=0
print(*pocket)