import sys
import itertools

arr = [list(map(str, sys.stdin.readline().rstrip().split())) for i in range(5)]
for i in range(5):
  arr[i] = list(itertools.chain.from_iterable(arr[i]))
maxlen = max(len(k) for k in arr)
for l in arr:
  while len(l) < maxlen:
    l.append("*")
#print(maxlen)
#for i in arr:
#  print(i)
for j in range(maxlen):
  for i in range(5):
    if arr[i][j] == '*':
      continue
    print(arr[i][j], end="")
