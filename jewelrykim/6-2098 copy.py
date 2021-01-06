# 외판원 순회
import sys
sys.stdin = open("week04/jewelrykim/6.txt",'r')
sys.setrecursionlimit(10**4)

city = int(sys.stdin.readline())
INF = 10**8
graph = []
dp_table = [[INF for _ in range(1 << city)] for _ in range(city)]
for _ in range(city):
    graph.append(list(map(int, sys.stdin.readline().split())))

def dfs(n, visited):
    if visited == (1 << city) - 1:
        if graph[n][0] == 0:
            return INF
        else:
            return graph[n][0]
    if dp_table[n][visited] != INF:
        return dp_table[n][visited]
    for i in range(1,city):
        if graph[n][i] != 0 and not visited & (1<<i):
            dp_table[n][visited] = min(dp_table[n][visited],
            dfs(i, visited | (1 <<i)) + graph[n][i])
    return dp_table[n][visited]

print(dfs(0,1))



        
