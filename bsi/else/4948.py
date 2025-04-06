import sys
lst = [True] * 123456
input = sys.stdin.readline


while k != 0:
    lst_sum = 0
    k = int(input())
    for i in range(1, k**0.5):
        for n in range(k // i):
            lst[i * n] = False

    for i in range(1, k):
        if lst[i] == True:
            lst_sum += 1
    
    print(lst_sum)