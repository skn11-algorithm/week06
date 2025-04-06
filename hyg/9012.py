import sys

n = int(sys.stdin.readline())

for i in range(n):
    str = sys.stdin.readline()
    stack = []
    flag = True
    
    for i,s in enumerate(str):
        if s == '\n':
           break
        
        if s == '(':
          stack.append(s)
        else:
            if len(stack)>0:
              stack.pop()
            else:
               flag = False
               break
    
    if len(stack)==0 and flag:
       print('YES')
    else:
       print('NO')