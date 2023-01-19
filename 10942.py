import sys
N=int(sys.stdin.readline())
n=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
dp=[[0]*N for x in range(N)]
for x in range(N):
    for start in range(N-x):
        end=start+x
        if start==end:
            dp[start][end]=1
        elif n[start]==n[end]:
            if start+1==end:
                dp[start][end]=1
            elif dp[start+1][end-1]==1:
                dp[start][end]=1
                
for x in range(M):
    s,e=map(int,sys.stdin.readline().split())
    print(dp[s-1][e-1])
