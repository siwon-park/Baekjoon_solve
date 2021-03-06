#이친수(2193번)
###################################
    # 문제: https://www.acmicpc.net/problem/2193
    # 다이나믹 프로그래밍
    # dp[N][0]의 의미: N자리 이진수의 끝자리가 0으로 끝난 경우의 수, dp[N][1]의 의미: N자리 이진수의 끝자리가 1로 끝난 경우의 수
    # 끝자리가 0인 N자리 이친수를 만들고자 한다면, N-1자리 이친수 중 0으로 끝났든, 1로 끝났든 상관없이 끝에 그냥 0을 붙이면 되고, (dp[N][0]=dp[N-1][0]+dp[N-1][1])
    # 끝자리가 1인 N자리 이친수를 만들려면, N-1자리 이친수 중 0으로 끝난 경우에 1을 붙이면 됨.(dp[N][1]=dp[N-1][0])
    # 위의 두가지 경우의 수를 더해서 dp[N][2]에 넣으면 끝
###################################
N=int(input())
dp=[[0,0,0] for i in range(N+1)]
dp[1][1],dp[1][2]=1,1
for i in range(2,N+1):
    dp[i][0]=dp[i-1][0]+dp[i-1][1]
    dp[i][1]=dp[i-1][0]
    dp[i][2]=dp[i][0]+dp[i][1]
print(dp[N][2])
