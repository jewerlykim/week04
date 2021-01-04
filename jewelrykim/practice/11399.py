# ATM
import sys
sys.stdin = open("week04/jewelrykim/practice/11399.txt", 'r')

people_num = int(sys.stdin.readline())
time_list = sorted(list(map(int, sys.stdin.readline().split())))
dp_table = [0 for _ in range(1001)]

for i in range(people_num):
    dp_table[i+1] = dp_table[i] + time_list[i]

print(sum(dp_table))
