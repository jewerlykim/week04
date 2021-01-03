# 피보나치 함수
import sys

test_case = int(sys.stdin.readline())
# 피보나치 함수선언
dp_table = [[0,0] for _ in range(41)]
dp_table[0] = [1,0]
dp_table[1] = [0,1]

for i in range(2,41):
    dp_table[i] = list(map(lambda x, y: x+y,dp_table[i-1],dp_table[i-2]))

# 테스트 케이스 출력
for _ in range(test_case):
    number = int(sys.stdin.readline())
    print(*dp_table[number])