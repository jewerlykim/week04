import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10000)
INF = 99
n = int(input())
mat = [list(map(int, input().split()))for _ in range(n)]
dp = [[INF]*(1 << n)for _ in range(n)]
def dfs(current, visit):
    if visit == (1 << n)-1:
        if mat[current][0] == 0:
            return INF
        else:
            return mat[current][0]
    if dp[current][visit] != INF:
        return dp[current][visit]
    for i in range(1, n):
        if not visit & (1 << i) and mat[current][i] != 0:
            dp[current][visit] = min(dp[current][visit], dfs(i, visit | (1 << i))+mat[current][i])
    return dp[current][visit]
print(dfs(0, 1))
for i in dp:
    print(i)