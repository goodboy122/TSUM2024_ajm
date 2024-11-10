import sys
sum=int(input())
count=int(input())
x=y=z=0
for i in range(count):
  x,y= map(int, sys.stdin.readline().split())
  z+=x*y
if sum==z:
  print("Yes")
else:
  print("No")