import sys
lst = [True] * 100000
input = sys.stdin.readline

for i in range(len(lst)):
    if i % 2 == 0:
        lst[i] = False

for i in range(int(len(lst) ** 5)):
    if lst[i] == True:
        for n in range(len(lst) // i):
            lst[n] == False


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
	## 홀수만 찾으면 되므로 2씩 더해준다.
    for i in range(3, int(n/2)+1, 2): 
        if lst[i] and lst[n-i]:
            print(f"{n} = {i} + {n-i}")
            break