import sys
size=int(sys.stdin.readline().rstrip())
l=list(map(int,sys.stdin.readline().split()))
v=int(sys.stdin.readline().rstrip())
print(l.count(v))