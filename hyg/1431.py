# input: 기타의 개수 n \n n개의 시리얼 번호 (중복x)
# output: 시리얼 번호 정렬하기

# 정렬 방법
# 1. 길이가 짧은 것
# 2. 길이가 같다면 모든 자리수의 합이 작은것 (숫자만 더하기)
# 3. 사전 순 비교 (숫자 < 알파벳)

import sys
input = sys.stdin.readline

def add_num(xs):
    result = 0
    for i in xs:
        if i.isdigit():
            result+=int(i)
    return result

if __name__ == '__main__':
    n = int(input())

    l = []
    for i in range(n):
        num = input().rstrip()
        l.append(num)

    l.sort(key = lambda x: (len(x), add_num(x), x))
    
    for i in l:
        print(i)

