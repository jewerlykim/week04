import sys
sys.stdin = open("week04/jewelrykim/test/2.txt", "r")
input=sys.stdin.readline

m, n = map(int, input().split())
zone=[]
for _ in range(m):
    line=input().split()
    zone.append(line)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
dp=[[0 for _ in range(n)] for _ in range(m)]
ans=0

def dsf(x,y):
    global ans
    if x == m-1 and y == n-1:
        ans +=1
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n and dp[nx][ny] ==0:
                if zone[nx][ny]<zone[x][y]:
                    dp[nx][ny] = 1
                    dsf(nx, ny)
                    dp[nx][ny]=0

dp[0][0] = 1
dsf(0,0)
print(ans)