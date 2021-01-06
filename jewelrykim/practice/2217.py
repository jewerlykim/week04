# 로프
import sys
rope_num = int(sys.stdin.readline())
ropes = []
for _ in range(rope_num):
    ropes.append(int(sys.stdin.readline()))
ropes.sort()

max_mass = 0
for i in range(rope_num):
    max_mass = max(max_mass, ropes[i] * (rope_num-i))

print(max_mass)