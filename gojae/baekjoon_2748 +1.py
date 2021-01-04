import sys

n= int(sys.stdin.readline().rstrip())

# 메모이제이션 활용(탑다운)
# memoization = [0] * 100
#
# def fibo(x):
#     if x == 1 or x == 2 :
#         return 1
#     # 이미 계산한 적 있다면 그 값을 그대로 반환
#     if memoization[x] !=0:
#         return memoization[x]
#     else :
#         memoization[x] = fibo(x-1) + fibo(x-2)
#         return memoization[x]
#
# print(fibo(n))


# dp테이블 활용(보텀업) - 이 걸 쓰자!
dp=[0]* 100

def fibo(x):
    for i in range(1, x+1):
        if i == 1 or i == 2:
            dp[i] = 1
        else :
            dp[i] = dp[i-1] + dp[i-2]

    return dp[x]


print(fibo(n))