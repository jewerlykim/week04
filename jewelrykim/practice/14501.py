# 퇴사
import sys
sys.stdin = open("week04/jewelrykim/practice/14501.txt",'r')
counsel_num = int(sys.stdin.readline())
counsel_schedule = [[0,0] for _ in range(counsel_num+1)]
for i in range(1,counsel_num+1):
    counsel_schedule[i][0], counsel_schedule[i][1] = map(int, sys.stdin.readline().split())

print(counsel_num, counsel_schedule)