import sys

arr = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
x = y = 0
max = arr[0][0]

for i in range(9):
  for j in range(9):
    if arr[i][j] >= max:
      max = arr[i][j]
      x = i + 1
      y = j + 1
print(max)
print(x, y)
