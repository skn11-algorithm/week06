import sys
input=sys.stdin.readline

s1=list(input().rstrip())
s2=list(input().rstrip())

s1_len=len(s1)
s2_len=len(s2)

# 문자 조합 비교하면서 수열 길이 저장
# LCS[i][j] = s2의 i번째 문자까지, s1의 j번째 문자까지 비교했을 때 LCS의 최대 길이
LCS=[[0]*(s1_len+1) for _ in range(s2_len+1)]


#s1과 s2의 모든 문자 조합을 비교하면서,
#지금까지 만든 LCS의 최대 길이를 점점 갱신

# s1 = ABC
# s2 = ACE 면                                            
#    ''  A  B  C (열 개수 = s1 길이)
# ''  0  0  0  0
# A   0  1  1  1
# C   0  1  1  2
# E   0  1  1  2

# 글자가 다르면 → 왼쪽이랑 위쪽 중 LCS 더 큰 값 가져오기
# 글자가 같으면 → 바로 앞 문자들까지 비교한 결과(대각선 왼쪽 위) + 1

for i in range(1,s2_len+1): #행 (s2 길이만큼)
    for j in range(1,s1_len+1): #열 (s1 길이만큼)
        if s1[j-1]==s2[i-1]: # 현재 글자가 같다면, 이전까지의 LCS + 1
            LCS[i][j]=LCS[i-1][j-1]+1
        else: # 다르다면 지금까지 만들어 온 LCS 중 더 긴 쪽을 선택
            LCS[i][j]=max(LCS[i][j-1],LCS[i-1][j])
        
print(LCS[-1][-1])