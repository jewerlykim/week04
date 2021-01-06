# 병든 나이트
import sys
import numpy as np
row, column = map(int, sys.stdin.readline().split())
visited = [[True for _ in range(column)] for _ in range(row)]
able_count = 1 # 처음 위치한 곳을 포함한 초기값
visited = np.array(visited)
# move_check(row-1,0)
def move_check(x, y):
    global able_count
    print(visited)
    # 위 위 오른쪽
    if x - 2 >= 0 and y + 1 <= column -1 and visited[x-2][y+1]:
        able_count += 1
        visited[x-2][y+1] = False
        move_check(x-2,y+1)
    # 위 오른쪽 오른쪽
    if x - 1 >= 0 and y + 2 <= column -1 and visited[x-1][y+2]:
        able_count += 1
        visited[x-1][y+2] = False
        move_check(x-1,y+2)
    # 아래 아래 오른쪽
    if x + 2 <= row-1 and y + 1 <= column -1 and visited[x+2][y+1]:
        able_count += 1
        visited[x+2][y+1] = False
        move_check(x+2,y+1)
    # 아래 오른쪽 오른쪽
    if x + 1 <= row-1 and y + 2 <= column -1 and visited[x+1][y+2]:
        able_count += 1
        visited[x+1][y+2] = False
        move_check(x+1,y+2)

move_check(row-1,0)
print(able_count)