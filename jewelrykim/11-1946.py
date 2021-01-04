# 신입사원
import sys
sys.stdin = open("week04/jewelrykim/11.txt",'r')
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    recruits = int(sys.stdin.readline())
    rank_list = []
    for _ in range(recruits):
        rank_list.append(list(map(int, sys.stdin.readline().split())))
    rank_list.sort()

    interview_criteria = rank_list[0][1]
    count = 0
    for i in range(1, recruits):
        if rank_list[i][1] > interview_criteria:
            count += 1
        else:
            interview_criteria = rank_list[i][1]
    
    print(recruits - count)