# 가장 큰 증가 부분 수열
import sys
sys.stdin = open("week04/jewelrykim/practice/11055.txt",'r')

# 입력 받기
N = int(sys.stdin.readline())
dp_table = [0 for _ in range(N)]

given_row = list(map(int, sys.stdin.readline().split()))
dp_table[0] = given_row[0]

for i in range(1,N):
    s = []
    for j in range(i-1,-1,-1):
        if given_row[i]>given_row[j]:
            s.append(dp_table[j])
    if not s:
        dp_table[i] = given_row[i]
    else:
        dp_table[i] = given_row[i] + max(s)
print(max(dp_table))