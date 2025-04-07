import sys

input = sys.stdin.readline

def divide_and_conquer(x, y, n):
    global white, blue
    color = paper[x][y]
    
    for xi in range(x, x+n):
        for yi in range(y, y+n):
            if color != paper[xi][yi]:
                divide_and_conquer(x, y, n//2)
                divide_and_conquer(x+n//2, y, n//2)
                divide_and_conquer(x, y+n//2, n//2)
                divide_and_conquer(x+n//2, y+n//2, n//2)
                return 
    
    if color == 0:
        white += 1
    else:
        blue += 1
        
if __name__ == '__main__':
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    white, blue = 0,0   
     
    divide_and_conquer(0,0,n)

    print(white, blue, sep='\n')        