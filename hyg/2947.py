import sys
input = sys.stdin.readline

def swap(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(' '.join(map(str, arr)))
            

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    
    while arr != [1,2,3,4,5]:
        swap(arr)
    