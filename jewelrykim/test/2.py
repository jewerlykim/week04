# 내리막길 
import sys
sys.setrecursionlimit(10**6)
row, column = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
dp_table = [[0 for _ in range(column)] for _ in range(row)]
count = 0
def dfs(x, y):
    global count
    # 주어진 범위를 벗어나느 경우에는 즉시 종료
    
    if x == row-1 and y == column-1:
        count += 1
    now_height = graph[x][y]
    if x-1>=0 and graph[x-1][y] < now_height:
        dfs(x-1,y)
    if x+1 <= row-1 and graph[x+1][y] < now_height:
        dfs(x+1,y)
    if y-1 >= 0 and graph[x][y-1] < now_height:
        dfs(x,y-1)
    if y+1 <= column - 1 and graph[x][y+1] < now_height:
        dfs(x,y+1)

dfs(0,0)
print(count)
    