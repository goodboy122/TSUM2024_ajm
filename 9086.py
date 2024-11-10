import sys

c = int(sys.stdin.readline().rstrip())
lists = []
for i in range(c):
  lists.append(sys.stdin.readline().rstrip())
for i in range(c):
  l = list(lists[i])
  print(l[0] + l[len(l) - 1])
