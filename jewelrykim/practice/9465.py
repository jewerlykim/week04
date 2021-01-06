# 스티커
import sys
sys.stdin = open("week04/jewelrykim/practice/9465.txt",'r')

test_case = int(sys.stdin.readline())
for i in range(test_case):
    column = int(sys.stdin.readline())
    paper = []
    for _ in range(2):
        paper.append(list(map(int, sys.stdin.readline().split())))
    paper[0][1] += paper[1][0]
    paper[1][1] += paper[0][0]
    for j in range(2,column):
        paper[0][j] += max(paper[1][j-1], paper[1][j-2])
        paper[1][j] += max(paper[0][j-1], paper[0][j-2])
    print(max(paper[0][column-1], paper[1][column-1]))