# 정수 삼각형
import sys
sys.stdin = open("week04/jewelrykim/practice/1932.txt", 'r')

size = int(sys.stdin.readline())
dp_table = [[0 for _ in range(size)] for _ in range(size)]
dp_table[0][0] = int(sys.stdin.readline())

for i in range(1,size):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(len(row)):
        if j:
            dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-1]) + row[j]
        else:
            dp_table[i][j] = dp_table[i-1][j] + row[j]

print(max(dp_table[-1]))
    