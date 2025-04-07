import sys
input = sys.stdin.readline

left_str = list(input().strip())
right_str = []

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'L':
        if left_str:
            right_str.append(left_str.pop())
    elif command[0] == 'D':
        if right_str:
            left_str.append(right_str.pop())
    elif command[0] == 'B':
        if left_str:
            left_str.pop()
    elif command[0] == 'P':
        left_str.append(command[1])

print(''.join(left_str + right_str[::-1]))