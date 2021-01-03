# 포도주 시식
import sys
# sys.stdin = open("week04/jewelrykim/practice/2156.txt",'r')

N = int(sys.stdin.readline())
wines = [0 for _ in range(10001)]
dp_table = [0 for _ in range(10001)]
for i in range(1,N+1):
    wines[i] = int(sys.stdin.readline())
dp_table[1]=wines[1]
dp_table[2]=wines[1]+wines[2]
dp_table[3]=max(wines[1]+wines[3], wines[2]+wines[3])
dp_table[4]=max(wines[1]+wines[2]+wines[4], wines[1]+wines[3]+wines[4])

for i in range(5, N+1):
    dp_table[i] = max(dp_table[i-3]+wines[i-1]+wines[i], dp_table[i-2]+wines[i], dp_table[i-4]+wines[i-1]+wines[i])

print(max(dp_table))