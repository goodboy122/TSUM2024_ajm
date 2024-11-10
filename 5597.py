import sys
student_list=[1]*30
for i in range(28):
  x=int(sys.stdin.readline().rstrip())
  student_list[x-1]=0
for i in range(30):
  if(student_list[i]==1):
    print(i+1)