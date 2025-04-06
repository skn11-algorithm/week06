# 인접한 애들은 같은색X
import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*1001

nums=list(map(int,input().rstrip().split()))
dp[1]=min(nums)
idx=nums.index(min(nums))

for i in range(2,n+1):
    nums=list(map(int,input().rstrip().split()))
    candidates=[(nums[j],j) for j in range(3) if j!=idx]
    val,new_idx=min(candidates)
    dp[i]=dp[i-1]+val
    idx=new_idx

print(dp[n])