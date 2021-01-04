import sys
sys.stdin = open("week04/jewelrykim/5.txt",'r')
import numpy as np

input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]
dp = np.array(dp)
for i in range(1, n):
    for j in range(n - i):
        x = j + i
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + s[j][0] * s[k][1] * s[x][1])
    print(dp)
print(dp[0][n - 1])