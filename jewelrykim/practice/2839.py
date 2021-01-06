# 설탕배달
import sys
N = int(sys.stdin.readline())

max_five = N // 5

for i in range(max_five, -1, -1):
    left = N - i * 5
    if left % 3 == 0:
        print(i+left//3)
        exit()
else:print(-1)
        