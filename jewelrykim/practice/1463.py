# 1로 만들기
import sys
N = int(sys.stdin.readline())
dp_table = [0 for _ in range(10**6 + 1)]
dp_table[2], dp_table[3] = 1, 1

for i in range(4,N+1):
    two_per = 10**6
    three_per = 10**6
    if i % 3 ==0:
        three_per = dp_table[i//3] + 1
    if i % 2 ==0:
        two_per = dp_table[i//2] + 1
    minus = dp_table[i-1] + 1
    dp_table[i] = min(minus, two_per, three_per)
    # print(i, dp_table[i])

print(dp_table[N])