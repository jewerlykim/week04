# 계단 오르기
import sys

stair_num = int(sys.stdin.readline())
stairs = [0 for _ in range(301)]
dp_table = [0 for _ in range(301)]

for i in range(stair_num):
    stairs[i]= int(sys.stdin.readline())

dp_table[0] = stairs[0]
dp_table[1] = stairs[0] + stairs[1]
dp_table[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, stair_num):
    dp_table[i] = max(dp_table[i-3] + stairs[i-1] + stairs[i], dp_table[i-2] + stairs[i])

print(dp_table[stair_num-1])

# ㅎㅣㅂ