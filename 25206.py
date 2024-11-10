import sys
grade={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
sum=0.0
p=0.0
for i in range(20):
  class_name,point,g=map(str,sys.stdin.readline().split())
  if(g=="P"):
    continue
  point=float(point)
  p+=point
  g=float(grade[g])
  sum+=(point*g)
print(sum/p)