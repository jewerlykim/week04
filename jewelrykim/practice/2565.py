# 전깃줄
import sys
sys.stdin = open("week04/jewelrykim/practice/2565.txt",'r')

n = int(sys.stdin.readline())
wires = []
wire_connect = []
dp_table = [0 for _ in range(n)]
for i in range(n):
    wires.append((list(map(int, sys.stdin.readline().split()))))
wires.sort(key= lambda x:x[0])
for i in range(n):
    wire_connect.append(wires[i][1])

print(wires)
print(wire_connect)
for i in range(n):
    for j in range(i):
        if wire_connect[i] > wire_connect[j] and dp_table[i] < dp_table[j]:
            dp_table[i] = dp_table[j]
    dp_table[i] += 1
    print(dp_table)

print(n-max(dp_table))