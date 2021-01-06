# 30
# 받은 문자열 중 0 이 없다면 무조건 -1
# 0이 하나라도 있으면 0이 맨끝 // 숫자의 합이 3의 배수라면 30의 배수/ 아니라면 -1 출력
# 다 통과했으면 가장 큰 순서대로 출력
import sys
N = list(map(str, sys.stdin.readline().rstrip()))

has_zero = '0' in N
sum = 0
for num in N:
    sum += int(num)

if not has_zero or sum%3:
    print(-1)
else:
    sor_N = sorted(N, reverse=True)
    print(*sor_N,sep='')