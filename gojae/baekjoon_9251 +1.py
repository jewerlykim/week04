import sys
sys.stdin = open('input.txt', 'r')

strings1= '0'+ sys.stdin.readline().rstrip()
strings2= '0'+ sys.stdin.readline().rstrip()

# string1이 세로축, string2가 가로축
dp=[[0 for _ in range(len(strings2))] for _ in range(len(strings1))]


for i in range(1, len(strings1)) :
    for j in range(1, len(strings2)) :
        if strings1[i]==strings2[j] :
            dp[i][j]=dp[i-1][j-1]+1
        else :
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])



print(dp[len(strings1)-1][len(strings2)-1])
