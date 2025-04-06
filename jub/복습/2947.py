n = list(map(int,input().split()))

#첫 순서는 1,2,3,4,5 가 아님
while n != [1,2,3,4,5]:

# 비교해서 바꿈, 버블 정렬

    for i in range(len(n)-1):
        for j in range(0,len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
                print(' '.join(map(str,n)))

