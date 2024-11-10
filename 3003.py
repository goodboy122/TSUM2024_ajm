import sys
chess=[1,1,2,2,2,8]
s=list(map(int,sys.stdin.readline().split()))
for i in range(6):
  s[i]=chess[i]-s[i]
print(*s)