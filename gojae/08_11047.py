import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, sys.stdin.readline().rstrip().split())

#문제에 모든 화폐가 그 전 화폐의 배수라는 말이 있어서 그리디 알고리즘으로 문제 풀이가 가능하다.

coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
count = 0

for coin in range(n-1, -1, -1):
    count += k//coins[coin]
    k = k%coins[coin]

print(count)
