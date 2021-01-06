# 카드 구매하기
# 자신을 뺀 나머지를 더했을때 나오는 최대값 , 자신이 곧 최대값 그중에서 최대값 
import sys
card_num = int(sys.stdin.readline())
dp_table = [0 for _ in range(1001)]

cards = list(map(int, sys.stdin.readline().split()))

for i in range(1, card_num+1):
    dp_table[i] = cards[i-1]
 
for i in range(2, card_num+1):
    max_count = 0
    for j in range(1,i):
        comp_num = i-j
        max_count = max(max_count, dp_table[j] + dp_table[i-j])
    dp_table[i] = max(max_count, cards[i-1])

print(max(dp_table))
