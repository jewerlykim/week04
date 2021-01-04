# 평범한 배낭
import sys
sys.stdin = open("week04/jewelrykim/4.txt", 'r')

number, weight_limit = map(int, sys.stdin.readline().split())
backpack = [[0,0]]
dp_table = [[0 for _ in range(weight_limit+1)] for _ in range(number+1)]
for _ in range(number):
    backpack.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, number+1):
    for j in range(1, weight_limit+1):
        if backpack[i][0] <= j:
            dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-backpack[i][0]]+backpack[i][1])
            pass
        else:
            dp_table[i][j] = dp_table[i-1][j]

print(dp_table[number][weight_limit])