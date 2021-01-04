# 행렬 곱셈 순서
import sys
sys.stdin = open("week04/jewelrykim/5.txt",'r')

N = int(sys.stdin.readline())
matrix = [[0,0]]
for _ in range(N):
    matrix.append(list(map(int,sys.stdin.readline())))

# for i in range(3, N+1):
#     dp_table[i] = dp_table[i-3] + min(matrix[i-2][0]*matrix[i-1][0]*matrix[i][1], matrix)