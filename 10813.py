import sys
n,m=map(int, sys.stdin.readline().split())
pocket=[i+1 for i in range(n)]
a=b=0;
for i in range(m):
  a,b=map(int, sys.stdin.readline().split())
  pocket[a-1],pocket[b-1]=pocket[b-1],pocket[a-1]
print(*pocket)