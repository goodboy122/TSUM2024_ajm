import sys
x=[25,10,5]
c=int(sys.stdin.readline().rstrip())
y=[[0]*5 for i in range(c)]
for i in range(c):
  y[i][4]=int(sys.stdin.readline().rstrip())
for i in range(c):
  for j in range(3):
    y[i][j]=y[i][4]//x[j]
    y[i][4]-=y[i][j]*x[j]
  y[i][3]=y[i][4]
  y[i].pop()
for i in range(c):
  print(*y[i])