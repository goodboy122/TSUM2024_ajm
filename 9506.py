import sys
x=0
Arr=[]
while x>=0:
  x=int(sys.stdin.readline().rstrip())
  if x==-1:
    break
  arr=[x]
  for i in range(1,(x//2)+1):
    if x%i==0:
      arr.append(i)
  Arr.append(list(arr))

for i in Arr:
  print(i[0],end="")
  if i[0]==(sum(i[1:])):
    print(" =", end=" ")
    print(" + ".join(map(str, i[1:])))
  else:
    print(" is NOT perfect.")
