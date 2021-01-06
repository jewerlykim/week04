# 대회 or 인턴
import sys
girls, boys, intern = map(int, sys.stdin.readline().split())

team_count = 0
while True:
    if girls + boys -3< intern or boys <=0 or girls <=0:
        break
    if girls >= 2 and boys >= 1:
        team_count += 1
        girls -= 2
        boys -= 1
    else:
        break

print(team_count)