import sys

r = 0
n, m = map(str, sys.stdin.readline().rstrip().split())
m = int(m)
n = list(n)
l = len(n)
for i in range(l):
  if n[i].isdigit():
    r += int(n[i]) * (m**(l - 1 - i))
  elif n[i].isupper():
    r += (10 + ord(n[i]) - ord('A')) * (m**(l - 1 - i))
  elif n[i].islower():
    r += (10 + ord(n[i]) - ord('a')) * (m**(l - 1 - i))
print(r)
