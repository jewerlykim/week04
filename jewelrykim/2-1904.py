# 01타일 결국 피보나치였음 수를 미리 나눠서 줄였더니 속도가 빨라졌다.
import sys
number = int(sys.stdin.readline()) # 100만 이하

dp_table = [0 for _ in range(1000001)]
dp_table[1] = 1
dp_table[2] = 2

for i in range(3,number+1):
    dp_table[i] = (dp_table[i-1] + dp_table[i-2])%15746

print(dp_table[number]%15746)