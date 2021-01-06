# 1,2,3 더하기 5
import sys
from collections import deque
test_case = int(sys.stdin.readline())

def bfs(num):
    count = 0
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()

        if x==num:
            count += 1
        elif x<num:
            for dx in (1,2,3):
                if dx!=y:
                    nx = x + dx
                    queue.append((nx,dx))
    return count


for i in range(test_case):
    n = int(sys.stdin.readline())
    print(bfs(n))