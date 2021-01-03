# 계단 오르기
import sys
sys.stdin = open("week04/jewelrykim/practice/2579.txt", 'r')

stair_num = int(sys.stdin.readline())
stairs = []
dp_table = [[] for _ in range(stair_num)]

for _ in range(stair_num):
    stairs.append(int(sys.stdin.readline()))

dp_table[0] = [stairs[0],1]
if stair_num>=2:
    dp_table[1] = [stairs[0] + stairs[1],2]
if stair_num>=3:
    dp_table[2] = max([stairs[0]+stairs[2],1], [stairs[1]+stairs[2],2])

for i in range(3, stair_num):
    if dp_table[i-1][1] == 2:
        dp_table[i] = [dp_table[i-2][0] + stairs[i], 1]
    else:
        if dp_table[i-1][0] > dp_table[i-2][0]:
            dp_table[i] = [dp_table[i-1][0]+stairs[i],2]
        else:
            dp_table[i] = [dp_table[i-2][0]+stairs[i],1]

print(dp_table[-1][0])