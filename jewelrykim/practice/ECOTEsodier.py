# 병사 배치하기
import sys
sys.stdin = open("week04/jewelrykim/practice/ECOTEsodier.txt", 'r')

sodiers = int(sys.stdin.readline())
sodiers_array = list(map(int, sys.stdin.readline().split()))
dp_table = [0 for _ in range(sodiers)]
print(sodiers_array)

for i in range(sodiers):
    for j in range(i):
        if sodiers_array[j]>sodiers_array[i] and dp_table[j]>=dp_table[i]:
            dp_table[i] = dp_table[j]
    dp_table[i] += 1
    print(dp_table)
print(sodiers-max(dp_table))