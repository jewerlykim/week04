# 못생긴 수
import sys
n = int(sys.stdin.readline())
dp_table = [True for _ in range(1001)]
dp_table[0] = False

for i in range(7, 1001):
    if dp_table[i] and i%2!=0 and i%3!=0 and i%5!=0:
        for j in range(i,1001,i):
            dp_table[j] = False
count = 0 
for i,v in enumerate(dp_table):
    if v:
        count += 1
    if count == n:
        print(i)
        break