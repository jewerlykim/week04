# 한 줄로 서기
import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

answer_list = [len(num_list)]
for i in range(len(num_list)-1,0,-1):
    answer_list.insert(num_list[i-1],i)
print(*answer_list)
