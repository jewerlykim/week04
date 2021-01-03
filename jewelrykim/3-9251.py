# LCS
import sys
sys.stdin = open("week04/jewelrykim/3.txt", 'r')

N = sys.stdin.readline().rstrip()
M = sys.stdin.readline().rstrip()
N_length = len(N)
M_length = len(M)

dp_table = [[0 for _ in range(M_length+1)] for _ in range(N_length+1)]

for i in range(1,N_length+1):
    for j in range(1,M_length+1):
        if N[i-1] == M[j-1]:
            dp_table[i][j] = dp_table[i-1][j-1] + 1
        else:
            dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

print(dp_table[-1][-1])