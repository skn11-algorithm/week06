import sys

input=sys.stdin.readline
n=int(input().rstrip()) # rstrip 안하니까 틀렸었음
strs=input().rstrip()
nums=[]
stack=[]

for _ in range(n):
    nums.append(int(input().rstrip()))

for s in strs:
    if 'A'<=s<='Z':
        stack.append(nums[ord(s)-ord('A')])
    else:
        x=stack.pop()
        y=stack.pop()

        if s=='*':
            stack.append(y*x)
        elif s=='/':
            stack.append(y/x)
        elif s=='+':
            stack.append(y+x)
        elif s=='-':
            stack.append(y-x)

result=stack.pop()
print("%.2f"%result)