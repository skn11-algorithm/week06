def divide_and_conquer(x,y,n):
    global arr
    if n==1:
        arr[x][y] = '*'
        return
        
    divide_and_conquer(x,y,n//3)
    divide_and_conquer(x+n//3,y,n//3)
    divide_and_conquer(x+(n//3)*2,y,n//3)
    
    divide_and_conquer(x,y+n//3,n//3)
    # divide_and_conquer(x+n//3,y+n//3,n//3)
    divide_and_conquer(x+(n//3)*2,y+n//3,n//3)
    
    divide_and_conquer(x,y+(n//3)*2,n//3)
    divide_and_conquer(x+n//3,y+(n//3)*2,n//3)
    divide_and_conquer(x+(n//3)*2,y+(n//3)*2,n//3)
    

if __name__ == '__main__':
    n = int(input())
    arr=[[' ' for j in range(n)] for i in range(n)]
    divide_and_conquer(0,0,n)
    
    for a in arr:
        for ai in a:
            print(ai, end='')
        print()
    