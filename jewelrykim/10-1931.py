# 회의실 배정
import sys
sys.stdin = open("week04/jewelrykim/10.txt",'r')

conference_num = int(sys.stdin.readline())
conference_list = []
for _ in range(conference_num):
    conference_list.append(list(map(int, sys.stdin.readline().split())))
conference_list.sort(key= lambda x: (x[1], x[0]))
# print(conference_list)

max_conferences = 1
end_time = conference_list[0][1]
for i in range(1, conference_num):
    if conference_list[i][0] >= end_time:
        max_conferences += 1
        end_time = conference_list[i][1]


print(max_conferences)