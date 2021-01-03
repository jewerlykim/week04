# RGB 거리
import sys
sys.stdin = open("week04/jewelrykim/practice/1149.txt", 'r')

house_num = int(sys.stdin.readline())

houses = []
dp_table = [[0 for _ in range(3)] for _ in range(house_num)]

for _ in range(house_num):
    houses.append(list(map(int, sys.stdin.readline().split())))

dp_table[0][0] = houses[0][0]
dp_table[0][1] = houses[0][1]
dp_table[0][2] = houses[0][2]

for i in range(1, house_num):
    for j in range(3):
        if j==0:
            dp_table[i][j] = min(dp_table[i-1][j+1], dp_table[i-1][j+2]) + houses[i][j]
        elif j==1:
            dp_table[i][j] = min(dp_table[i-1][j-1], dp_table[i-1][j+1]) + houses[i][j]
        else:
            dp_table[i][j] = min(dp_table[i-1][j-2], dp_table[i-1][j-1]) + houses[i][j]

print(min(dp_table[-1]))
