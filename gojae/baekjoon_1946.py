import sys
sys.stdin = open('input.txt', 'r')

testcases = int(sys.stdin.readline().rstrip())

for _ in range(testcases):
    n= int(sys.stdin.readline().rstrip())
    passes=[]
    rankings=[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    rankings.sort()
    print(rankings)
    for i in range(1, len(rankings)) :
        if rankings[i][0]<rankings[0][0] or rankings[i][1]<rankings[0][1] :
            passes.append([rankings[i][0], rankings[i][1]])
    rankings.sort(key=lambda x : x[1])
    print(rankings)
    for i in range(1, len(rankings)) :
        if rankings[i][0]<rankings[0][0] or rankings[i][1]<rankings[0][1] :
            if [rankings[i][0], rankings[i][1]] not in passes:
                passes.append([rankings[i][0], rankings[i][1]])
    print(passes)
    print(len(passes))