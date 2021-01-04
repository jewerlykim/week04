# 주유소
import sys
sys.stdin = open("week04/jewelrykim/practice/13305.txt",'r')

city_num = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
city_gas = list(map(int, sys.stdin.readline().split()))


gas_price = city_gas[0]
min_cost = 0

for i in range(city_num-1):
    min_cost += distances[i] * gas_price
    if gas_price > city_gas[i+1] and i+1 != city_num-1:
        gas_price = city_gas[i+1]

print(min_cost)