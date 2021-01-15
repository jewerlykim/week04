# 내리막길 
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("week04/jewelrykim/test/2.txt",'r')
import numpy as np
row, column = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
dp_table = [[0 for _ in range(column)] for _ in range(row)]
count = 0
dp_table[0][0] = 1
dp_table = np.array(dp_table)
for i in range(row):
    for j in range(column):
        if i-1 >= 0 and dp_table[i-1][j] > dp_table[i][j]:
            dp_table[i][j] += dp_table[i-1][j]
        if i+1 <= row-1 and dp_table[i+1][j] > dp_table[i][j]:
            dp_table[i][j] += dp_table[i+1][j]
        if j-1 >= 0 and dp_table[i][j-1] > dp_table[i][j]:
            dp_table[i][j] += dp_table[i][j-1]
        if j+1 <= column-1 and dp_table[i][j+1] > dp_table[i][j]:
            dp_table[i][j] += dp_table[i][j+1]
print(dp_table[row-1][column-1])
print(dp_table)