import sys

xy = [[0] * 100 for i in range(100)]
result = 0
c = int(sys.stdin.readline().rstrip())
for i in range(c):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  for i in range(x, x + 10):
    for j in range(y, y + 10):
      xy[i][j] = 1
for i in xy:
  result += sum(i)
print(result)
