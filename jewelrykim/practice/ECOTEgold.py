# 금광
import sys
import numpy as np
sys.stdin = open("week04/jewelrykim/practice/ECOTEgold.txt",'r')

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    gold_mine = []
    row, column = map(int, sys.stdin.readline().split())
    max_mine = [[0 for _ in range(column)] for _ in range(row)]
    
    columns = list(map(int, sys.stdin.readline().split()))

    for i in range(row):
        gold_mine.append(columns[i*column:(i+1)*column])
    
    gold_mine = np.array(gold_mine)
    max_mine = np.array(max_mine)
    for i in range(row):
        max_mine[i][0] = gold_mine[i][0]

    for i in range(1, column):
        for j in range(row):
            up_gold = 0
            mid_gold = 0
            down_gold = 0
            if j-1>=0:
                up_gold=max_mine[j-1][i-1]
            if j+1<row:
                down_gold=max_mine[j+1][i-1]
            mid_gold=max_mine[j][i-1]
            max_mine[j][i] = max(up_gold, mid_gold, down_gold) + gold_mine[j][i]
    
    max_gold = max_mine[0][column-1]
    for i in range(1,row):
        max_gold = max(max_gold, max_mine[i][column-1])
    
    print(max_gold)

