import sys

n, m = map(int, sys.stdin.readline().split())
pocket = [i + 1 for i in range(n)]
min = max = 0
for i in range(m):
  min, max = map(int, sys.stdin.readline().split())
  for j in range((max - min + 1) // 2):
    pocket[min - 1 + j], pocket[max - 1 - j] = pocket[max - 1 -
                                                      j], pocket[min - 1 + j]
print(*pocket)
