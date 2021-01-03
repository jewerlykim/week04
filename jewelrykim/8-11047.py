# 동전 0
import sys
sys.stdin = open("week04/jewelrykim/8.txt",'r')
coin_num, value = map(int, sys.stdin.readline().split())
coins = []
for _ in range(coin_num):
    coins.append(int(sys.stdin.readline()))
reversed_coins = sorted(coins, reverse=True)
# print(reversed_coins)
coin_count = 0

for coin in reversed_coins:
    if value // coin > 0:
        coin_count += value // coin 
        value %= coin

print(coin_count)