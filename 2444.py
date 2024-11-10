import sys
s=int(sys.stdin.readline().rstrip())
for i in range(s):
  i=i+1
  for j in range(s-i):
    print(" ",end="")
  for k in range(i*2-1):
    print("*",end="")
  print()
for i in range(s-1,0,-1):
  for j in range(s-i):
    print(" ",end="")
  for k in range(i*2-1):
    print("*",end="")
  print()