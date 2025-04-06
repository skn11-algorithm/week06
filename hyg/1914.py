import sys
input = sys.stdin.readline

def hanoi(n, start, end):
    if n == 1 :
        print(start, end)
        return
     
    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)
            

if __name__ == '__main__':
    n = int(input())
    print(2**n-1)
    if n <= 20 :
        hanoi(n, 1, 3)
        