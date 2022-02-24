# 득수야 밥먹자(24464번)
#############################################################
    # 문제: https://www.acmicpc.net/problem/24464
    # DP(다이나믹 프로그래밍)
    # 객관적인 난이도는 낮았으나, 개인적으로는 점화식을 찾는데 엄청 어려웠던 문제였음
    # 정확히 말하면 규칙성은 찾았으나, 점화식을 찾기가 까다로웠다. 특히 연속으로 식당을 가는 경우에 대해 규칙성은 찾았으나 점화식을 찾기 힘들었다.
    # 그림을 그려서 해결했는데, 일단 표현을 하자면 배열의 의미는 각각 [굶음, 굶고 다음날 식당, 연속으로 식당, 합]이다.
    # 굶는 경우의 수는 전날 굶지 않는 경우의 수이고, 굶고 다음날 식당가는 경우는 굶운 경우의 수 x4이다.
    # 연속으로 식당에 가는 경우의 수는 전날 모든 경우의 수의 합 + 전전날 굶은 경우x2의 합이다.
    # 사실 연속으로 식당에 가는 경우의 수가 이렇게 되는 이유를 자세히 쓰자면 전날 굶고 식당에 가는 경우의 수 *(3/2) + 전날 연속으로 식당에 간 경우의 수 + 전날 굶은 경우의 수이다.
    # 직접 그려보면서 하면 그렇게 된다.
    # 그런데 중요한 것은 저렇게 점화식을 짜면 틀렸습니다가 나오는데,
    # 3/2인 경우 float형이 되고, 그러자고 정수형 출력을 위해 3*경우의 수 // 2를 하면 버림이 발생하여 답이 제대로 안 나오는 게 되는 경우가 발생한다.
#############################################################
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, 0, 0, 0] for i in range(N+2)]
dp[1] = [1, 4, 0, 5]
dp[2] = [4, 4, 6, 14]
for i in range(3, N+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000007
    dp[i][1] = (4*dp[i-1][0]) % 1000000007
    dp[i][2] = (2*dp[i-2][0] + dp[i-1][3]) % 1000000007
    dp[i][3] = (dp[i][0] + dp[i][1] + dp[i][2]) % 1000000007
print(dp[N][3])
