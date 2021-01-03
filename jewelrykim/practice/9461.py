# 파도반 수열 자기 전전항 + 전전전항을 더하면 나옴.
import sys
test_case = int(sys.stdin.readline())
# dp 테이블
dp_table = [1 for _ in range(101)]

for i in range(4, 101):
    dp_table[i] = dp_table[i-2] + dp_table[i-3]

# 출력
for _ in range(test_case):
    print(dp_table[int(sys.stdin.readline())])