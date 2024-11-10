import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
d = []
r = ""
while n > 0:
  d.append(int(n % m))
  n = n // m
d.reverse()
for x in d:
  if x >= 10:
    r += (chr(x + ord('A') - 10))
  else:
    r += str(x)
print(r)
