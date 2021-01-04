# 평범한 배낭
import sys
sys.stdin = open("week04/jewelrykim/4.txt", 'r')

number, weight_limit = map(int, sys.stdin.readline().split())
dp_table = [0 for _ in range(25)]
for _ in range(number):
    x , y = map(int, sys.stdin.readline().split())
    dp_table[x] = y

print(dp_table)
for i in range(3, weight_limit+1):
    max_num = 0
    if i%2:
        for j in range(1, i//2+1):
            dp_table[i] = max(dp_table[i], dp_table[j]+dp_table[i-j])
    else:
        for j in range(1, i//2):
            dp_table[i] = max(dp_table[i], dp_table[j]+dp_table[i-j])

print(dp_table)

