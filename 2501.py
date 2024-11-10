import sys

x, y = map(int, sys.stdin.readline().rstrip().split())
counter = ans = c = 0
for i in range(1, x + 1):
  if x % i == 0:
    counter += 1
    if counter == y:
      print(i)
      c = i
      break
if c == 0:
  print(c)
