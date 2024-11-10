import sys

x, y = 1, 1
ans = []
while x > 0 and y > 0:
  x, y = map(int, sys.stdin.readline().rstrip().split())
  if x == 0 and y == 0:
    break
  if y % x == 0:
    ans.append('factor')
  elif x % y == 0:
    ans.append('multiple')
  elif x == y:
    ans.append('bother')
  else:
    ans.append('neither')
for i in ans:
  print(i)
